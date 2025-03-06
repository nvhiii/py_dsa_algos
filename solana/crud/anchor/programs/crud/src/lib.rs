#![allow(clippy::result_large_err)]

use anchor_lang::prelude::*;

declare_id!("7uQKYAJmfWnKXB76ApyyKd4n4BRNL2RZ2gPcKTSYLymn");

pub const ANCHOR_DISCRIMINATOR_SIZE: usize = 8;

#[program]
pub mod crud {

  use super::*;

  // C(reate)
  pub fn create_journal_entry(ctx: Context<CreateEntry>, title: String, message: String) -> Result<()> {

    let journal_entry = &mut ctx.accounts.journal_entry;
    journal_entry.owner = ctx.accounts.owner.key();
    journal_entry.title = title;
    journal_entry.message = message;
    Ok(())

  }

  // R(read) is just for reading from blockchain, pretty self explanatory given seeds and program itself

  // U(pdate)

  pub fn update_journal_entry(ctx: Context<UpdateEntry>, _title: String, message: String) -> Result<()> {

    let journal_entry = &mut ctx.accounts.journal_entry;
    journal_entry.message = message; // updating the message! 
    Ok(())

  }

  // D(elete)

  pub fn delete_journal_entry(_ctx: Context<DeleteEntry>, _title: String) -> Result<()> {

    Ok(())

  }

}

#[derive(Accounts)]
#[instruction(title: String, message: String)]
pub struct UpdateEntry<'info> {

  #[account(
    mut,
    realloc = ANCHOR_DISCRIMINATOR_SIZE + JournalEntryState::INIT_SPACE,
    realloc::payer = owner,
    realloc::zero = true,
    seeds = [owner.key().as_ref(), title.as_bytes()],
    bump
  )]
  pub journal_entry: Account<'info, JournalEntryState>,

  #[account(mut)]
  pub owner: Signer<'info>,

  pub system_program: Program<'info, System>,

}

// validation struct
#[derive(Accounts)]
#[instruction(title: String)]
pub struct CreateEntry<'info> {

  #[account(

    init,
    payer = owner,
    space = ANCHOR_DISCRIMINATOR_SIZE + JournalEntryState::INIT_SPACE,
    seeds = [owner.key().as_ref(), title.as_bytes()],
    bump

  )]
  pub journal_entry: Account<'info, JournalEntryState>,

  // need sys program
  #[account(mut)]
  // since this is the account that will be paying, it must be mutable!
  pub owner: Signer<'info>,

  pub system_program: Program<'info, System>,

}

#[derive(Accounts)]
#[instruction(title: String)]
pub struct DeleteEntry<'info> {

  #[account(
    mut,
    seeds = [owner.key().as_ref(), title.as_bytes()],
    bump,
    // adding a close constraint will close the account
    close = owner,
  )]
  pub journal_entry: Account<'info, JournalEntryState>,

  #[account(mut)]
  pub owner: Signer<'info>, // we need the owner acc because the seed requires it 

  pub system_program: Program<'info, System>,

}

#[account]
#[derive(InitSpace)]
pub struct JournalEntryState {

  pub owner: Pubkey,
  #[max_len(50)]
  pub title: String,
  #[max_len(1000)]
  pub message: String,

}

