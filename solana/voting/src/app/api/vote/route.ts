import { ActionGetResponse, ActionPostRequest, ACTIONS_CORS_HEADERS, createPostResponse } from "@solana/actions";
import { Connection, PublicKey, Transaction,  } from "@solana/web3.js";
import { Voting } from "@/../anchor/target/types/voting";
import { AnchorProvider, BN, Program } from "@coral-xyz/anchor";

const IDL = require("@/../anchor/target/idl/voting.json")

// in this example, we are implementing blinks and actions via the api
// first user interacts, then a get req sent to api
// then api sends back a response with all the actions
// user sees all actions from metadata in the ui
// then user interacts with the ui to send a post req to api
// after this, the api is a bit diff from typical rest api, since it deals with wallets and serialized transactions on chain

// the get request is what the user submit
export async function GET(request: Request) {

  // this is the get response
  // action basically, blink is the fancy way of saying the frontend ui
  const actionMetaData: ActionGetResponse = {

    // in the response, we must specify what we really want in the interface
    icon: "https://zestfulkitchen.com/wp-content/uploads/2021/09/Peanut-butter_hero_for-web-2.jpg",
    title: "Vote for your favorite type of peanut butter",
    description: "Vote between crunchy and smooth peanut butter",
    label: "Vote",
    // since the above alone only allows for one action, we need to add links,
    // in order to give the user the choice of what action that they want to do.
    links: {
      actions: [

        //the user ui that the user will be shown
        {
          type: "post",
          href: "/api/vote?candidate=Crunchy", // this is the api endpoint
          label: "Crunchy",
        },
        {
          type: "post", // ensure all params are the same as the actions param
          href: "/api/vote?candidate=Smooth",
          label: "Smooth",
        }

      ]
    }

  }
  // the actions sdk provides a cors header bypass for testing, which can be parameterized in the json response
  // when testing blinks, phantom or other wallets will tell you that a certain action is not registered,
  // need to ensure the action is registered in order for it to truly work
  return Response.json(actionMetaData, { headers : ACTIONS_CORS_HEADERS});
}

// this is the options to return the request
export const OPTIONS = GET;
// when we test on the blink, we expect the post to fail, since we havent created it fully yet

export async function POST(request: Request) {

  const url = new URL(request.url);
  const candidate = url.searchParams.get("candidate");

  if (candidate != "Crunchy" && candidate != "Smooth") {
    return new Response("Invalid candidate", { status: 400, headers: ACTIONS_CORS_HEADERS});
  }

  // time for blockhash, message, and signatures if needed in server side
  const connection = new Connection("http://127.0.0.1:8899", "confirmed"); // commitment status
  // this can be processed, confirmed, and finalized. to date, confirmed almost always goes to finalized
  // need to create a provider from anchor here as well!
  const program: Program<Voting> = new Program(IDL, {connection});

  // now grab all the info needed from the URL via the payload in post req
  const body: ActionPostRequest = await request.json();
  let voter;

  // we are ensuring the account key is valid from the body of the req
  try {

    voter = new PublicKey(body.account);

  } catch (error) {

    return new Response("Invalid account", { status: 400, headers: ACTIONS_CORS_HEADERS});

  }

  // now we grab instructions
  const instruction = await program.methods.vote(candidate, new BN(1))
  .accounts({
    signer: voter,

  })
  .instruction();

  // now blockhash
  const blockhash = await connection.getLatestBlockhash();

  // transaction
  const transaction = new Transaction({
    feePayer: voter,
    blockhash: blockhash.blockhash,
    lastValidBlockHeight: blockhash.lastValidBlockHeight, 
  }).add(instruction);

  const response = await createPostResponse({
    fields: {
      transaction: transaction,
    }
  });

  return Response.json(response, { headers: ACTIONS_CORS_HEADERS });

}