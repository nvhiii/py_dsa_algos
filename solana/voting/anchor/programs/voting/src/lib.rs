#![allow(clippy::result_large_err)]

use anchor_lang::prelude::*;

declare_id!("coUnmi3oBUtwtd9fjeAvSsJssXh5A5xyPbhpewyzRVF");

// So what will we be needing for this project?
// we need the poll questio acc (account model = data struct)
// we need the candidates acc (for the various answers to the poll)
// we also need need instructions for the said structs, need to init the poll, as well as the candidate
// poll, candidate, and the voting instruction

pub const ANCHOR_DISCRIMINATOR_SIZE: usize = 8;

#[program] // this macro is for the anchor smart contract
pub mod voting {

  use super::*;

  // instruction handlers, to work around the data structures
  pub fn initialize_poll(ctx: Context<InitializePoll>,
                          poll_id: u64,
                          description: String,
                          poll_start: u64,
                          poll_end: u64) -> Result<()> {
    
    let poll = &mut ctx.accounts.poll;
    poll.poll_id = poll_id;
    poll.description = description;
    poll.poll_start = poll_start;
    poll.poll_end = poll_end;
    poll.candidate_amount = 0; // this is a counter, so we dont init in the poll instance itself
    Ok(())

  }

  // what we need for the candidate validation struct
  // we are not actually using 
  pub fn initialize_candidate(ctx: Context<InitializeCandidate>,
                              candidate_name: String,
                              _poll_id: u64) -> Result<()> {

    let candidate = &mut ctx.accounts.candidate;
    let poll = &mut ctx.accounts.poll;
    poll.candidate_amount += 1;
    candidate.candidate_name = candidate_name;
    candidate.candidate_votes = 0;
    Ok(())                            
  }

  // our instruction handler for voting for each candidate the poll
  pub fn vote(ctx: Context<Vote>, _candidate_name: String, _poll_id: u64) -> Result<()> {

    let candidate = &mut ctx.accounts.candidate;
    candidate.candidate_votes += 1;
    
    Ok(())

  }

  

}

// these are for initializing our structs, not the structs themselves
// the reason we have lifetime on this account is simply bc we need it for the initializer
// this is a "validation struct, not the actual struct"
#[derive(Accounts)]
#[instruction(poll_id: u64)] // using the instruction macro allows us to pull certain params from the instruction handlers
pub struct InitializePoll<'info> {

  // fill in later
  #[account(mut)]
  pub signer: Signer<'info>,
  // after creating the initialization method, we need to create the struct, then we can fill in the init params
  #[account(

    init,
    payer = signer,
    space = ANCHOR_DISCRIMINATOR_SIZE + Poll::INIT_SPACE,
    seeds = [poll_id.to_le_bytes().as_ref()],
     // to le bytes basically puts it in log10 formatting
    bump,
  )]
  pub poll: Account<'info, Poll>,

  pub system_program: Program<'info, System>,

}

// validation struct for the candidates struct
#[derive(Accounts)]
#[instruction(candidate_name: String, poll_id: u64)] // these are needed for the seed
pub struct InitializeCandidate<'info> {

  // fill in later
  #[account(mut)]
  pub signer: Signer<'info>,

  // since this is the validation struct for the candidates, we do not need to create it, just reference it via seed and bump
  #[account(
    mut,
    seeds = [poll_id.to_le_bytes().as_ref()],
     // to le bytes basically puts it in log10 formatting
    bump,
  )]
  pub poll: Account<'info, Poll>,

  #[account(

    init,
    payer = signer,
    space = ANCHOR_DISCRIMINATOR_SIZE + Candidate::INIT_SPACE,
    seeds = [poll_id.to_le_bytes().as_ref(), candidate_name.as_bytes().as_ref()],
    bump,

  )]
  pub candidate: Account<'info, Candidate>,

  pub system_program: Program<'info, System>,
}

// here will be the validation struct for the votes
#[derive(Accounts)]
#[instruction(candidate_name: String, poll_id: u64)]
pub struct Vote<'info> {

  // fill in later
  // will not be mutable because we arent paying for it
  pub signer: Signer<'info>,

  // since this is the validation struct for the candidates, we do not need to create it, just reference it via seed and bump
  #[account(
    seeds = [poll_id.to_le_bytes().as_ref()],
     // to le bytes basically puts it in log10 formatting
    bump,
  )]
  pub poll: Account<'info, Poll>,

  #[account(
    mut,
    seeds = [poll_id.to_le_bytes().as_ref(), candidate_name.as_bytes().as_ref()],
    bump,

  )]
  pub candidate: Account<'info, Candidate>,

}

// actual poll struct
#[account]
#[derive(InitSpace)]
pub struct Poll {

  pub poll_id: u64,
  #[max_len(280)]
  pub description: String,
  pub poll_start: u64,
  pub poll_end: u64,
  pub candidate_amount: u64,
}

// tba is the candidates struct here
#[account]
#[derive(InitSpace)]
pub struct Candidate {

  // how come we dont use the params from the instruction handler in the struct itself?
  // this is because the seed needed to identify the candidate account needs the poll id, not the struct itself
  #[max_len(32)]
  pub candidate_name: String,
  pub candidate_votes: u64,

}