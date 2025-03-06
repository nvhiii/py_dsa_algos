import { startAnchor } from 'solana-bankrun'
import { BankrunProvider } from 'anchor-bankrun'
import * as anchor from '@coral-xyz/anchor'
import { Program } from '@coral-xyz/anchor'
import { Keypair, PublicKey } from '@solana/web3.js'

// need type and the interface before testing anyhting, these are both in types and the idl directories in the anchor dir
// the idl gives us all the info about the program in json format.
// we also need to import the program type, which is located at the target types
import { Voting } from '../target/types/voting'

// we need to grab the idl from the anchor target idl path
const IDL = require('../target/idl/voting.json');

// this key is from the smart contract from anchor
const votingAddress = new PublicKey("coUnmi3oBUtwtd9fjeAvSsJssXh5A5xyPbhpewyzRVF");

describe('voting', () => {

  // since we will have multiple integration tests, we can set all contexts beforehand
  let context;
  let provider;
  let votingProgram: anchor.Program<Voting>;

  beforeAll(async () => {

    // in order to create the context, we dont need the path, as it is already auto read, but in our case, we do want the 
    // other params in the start anchor, particularly the extra programs here. in order to feed in
    // those programs, we must look into the startanchor then the extra programs methods, and pass them in as a key val map
    context = await startAnchor("", [{name: "voting", programId: votingAddress}], []);
    provider = new BankrunProvider(context);

    // here, we instantiate the program with json and the testing provider
    votingProgram = new Program<Voting>(

      IDL,
      provider

    );

  })

  it('Initialize Voting', async () => {

    // if the generated idl is not recognizing all params, make sure to anchor build again!
    // now, we want to be able to use the methods using the testing framework
    await votingProgram.methods.initializePoll(

      // to do the unsigned ints in typescript, use anchor.BN
      new anchor.BN(1), // the poll id
      "What is your favorite type of peanut butter?", // string
      new anchor.BN(0), // start time
      new anchor.BN(1841025500), // end time

    ).rpc();

    // we must pull that account
    // to find the pda, we need to look at the seeds for the poll validation struct
    const [pollAddress] = PublicKey.findProgramAddressSync(
      [new anchor.BN(1).toArrayLike(Buffer, 'le', 8)],
      votingAddress
    );

    // basically we are fetching poll address off of this address
    const poll = await votingProgram.account.poll.fetch(pollAddress);
    console.log(poll);

    // up until now, we didnt really test + expect values, we just checked if accounts worked properly w/ appropriate values
    expect(poll.pollId.toNumber()).toEqual(1);
    expect(poll.description).toEqual("What is your favorite type of peanut butter?");
    expect(poll.pollStart.toNumber()).toBeLessThan(poll.pollEnd.toNumber());

  });

  // new integration test for the candidate
  it('Initialize Candidate', async () => {
    
    await votingProgram.methods.initializeCandidate(
      "Smooth",
      new anchor.BN(1),
    ).rpc();                
    await votingProgram.methods.initializeCandidate(
      "Crunchy",
      new anchor.BN(1),
    ).rpc();

    // now, lets pull the accounts for the candidates!
    // first need to check the seeds and the order they are in
    const [smoothAddress] = PublicKey.findProgramAddressSync(
      [new anchor.BN(1).toArrayLike(Buffer, 'le', 8), Buffer.from("Smooth")],
      votingAddress
    )
    const smooth = await votingProgram.account.candidate.fetch(smoothAddress);
    expect(smooth.candidateVotes.toNumber()).toEqual(0); // want 0, to ensure no cheating

    const [crunchyAddress] = PublicKey.findProgramAddressSync(
      [new anchor.BN(1).toArrayLike(Buffer, 'le', 8), Buffer.from("Crunchy")],
      votingAddress
    )
    const crunchy = await votingProgram.account.candidate.fetch(crunchyAddress);
    expect(crunchy.candidateVotes.toNumber()).toEqual(0);

    console.log(smooth, crunchy);

  })

  it('Vote', async () => {

    // example of what instruction should be like
    await votingProgram.methods.vote(
      "Smooth",
      new anchor.BN(1),
    ).rpc(); // here, we are not using actual persons pubkey, but as rpc call!

    const [smoothAddress] = PublicKey.findProgramAddressSync(
      [new anchor.BN(1).toArrayLike(Buffer, 'le', 8), Buffer.from("Smooth")],
      votingAddress
    )
    const smooth = await votingProgram.account.candidate.fetch(smoothAddress);
    expect(smooth.candidateVotes.toNumber()).toEqual(1); // want 0, to ensure no cheating

    console.log(smooth);

  })

});
