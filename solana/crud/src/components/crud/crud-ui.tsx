'use client'

import { PublicKey } from '@solana/web3.js'
// import { useMemo } from 'react'

import { useCrudProgram, useCrudProgramAccount } from './crud-data-access'
import { useMemo, useState } from 'react'
import { useWallet } from '@solana/wallet-adapter-react';

export function CrudCreate() {
  const [title, setTitle] = useState('');
  const [message, setMessage] = useState('');
  const { createEntry } = useCrudProgram();
  const { publicKey } = useWallet();

  // validation check
  const isFormValid = title.trim() !== "" && message.trim() !== "";

  // now handle submit from frontend to our data access in front to back
  const handleSubmit = () => {

    if (publicKey && isFormValid) {

      createEntry.mutateAsync({ owner: publicKey, title, message });

    }

  };

  // case where user doesnt have key connected (no wallet)
  if (!publicKey) { 

    return <p>Connect your wallet.</p>

  }

  return (
    <div>

      <input 
      type="text"
      placeholder="Title"
      value={title}
      onChange={(e) => setTitle(e.target.value)}
      className="input input-bordered w-full max-w-xs"
      />

      <textarea
      placeholder="Message"
      value={message}
      onChange={(e) => setMessage(e.target.value)}
      className="textarea textarea-bordered w-full max-w-xs"
      />

      <button
      onClick={handleSubmit}
      disabled={createEntry.isPending || !isFormValid}
      className="btn btn-xs lg:btn-md btn-primary"
      />

    </div>
  )
}

export function CrudList() {
  const { accounts, getProgramAccount } = useCrudProgram()

  if (getProgramAccount.isLoading) {
    return <span className="loading loading-spinner loading-lg"></span>
  }
  if (!getProgramAccount.data?.value) {
    return (
      <div className="alert alert-info flex justify-center">
        <span>Program account not found. Make sure you have deployed the program and are on the correct cluster.</span>
      </div>
    )
  }
  return (
    <div className={'space-y-6'}>
      {accounts.isLoading ? (
        <span className="loading loading-spinner loading-lg"></span>
      ) : accounts.data?.length ? (
        <div className="grid md:grid-cols-2 gap-4">
          {accounts.data?.map((account) => (
            <CrudCard key={account.publicKey.toString()} account={account.publicKey} />
          ))}
        </div>
      ) : (
        <div className="text-center">
          <h2 className={'text-2xl'}>No accounts</h2>
          No accounts found. Create one above to get started.
        </div>
      )}
    </div>
  )
}

function CrudCard({ account }: { account: PublicKey }) {
  const { 
    accountQuery, updateEntry, deleteEntry 
  } = useCrudProgramAccount({ account })

  const { publicKey } = useWallet();

  const [ message, setMessage ] = useState("");
  const title = accountQuery.data?.title;

  // validation check
  const isFormValid = message.trim() !== "";

  // now handle submit from frontend to our data access in front to back
  const handleSubmit = () => {

    if (publicKey && isFormValid && title) {

      updateEntry.mutateAsync({ owner: publicKey, title, message });

    }

  };

  // case where user doesnt have key connected (no wallet)
  if (!publicKey) { 

    return <p>Connect your wallet.</p>

  }
            
  return accountQuery.isLoading ? (
    <span className="loading loading-spinner loading-lg"></span> ) : (
      <div className="card card-bordered border-base-300 border-4 text-neutral-content">
        <div className="card-body items-center text-center">
          <div className="space-y-2"></div>
          <h2 className="card-title justify-center text-3xl cursor-pointer" onClick={() => accountQuery.refetch()}>
            {accountQuery.data?.title}</h2>
          {/* add in message here */}
          <p>{accountQuery.data?.message}</p>
          <div className="card-actions justify-around">
            <textarea
            placeholder="Message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            className="textarea textarea-bordered w-full max-w-xs"
            />
            <button
            onClick={handleSubmit}
            disabled={updateEntry.isPending || !isFormValid}
            className="btn btn-xs lg:btn-md btn-primary"
            >
              Update Journal
            </button>
            <button
              onClick={() => {

                const title = accountQuery.data?.title;

                if (title) {
                  deleteEntry.mutateAsync(title);
                }

              }
            }
            >
              Delete Journal</button>
          </div>

        </div>
      </div>
    )

}
