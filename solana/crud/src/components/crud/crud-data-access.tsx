'use client'

import { getCrudProgram, getCrudProgramId } from '@project/anchor'
import { useConnection } from '@solana/wallet-adapter-react'
import { Cluster, Keypair, PublicKey } from '@solana/web3.js'
import { useMutation, useQuery } from '@tanstack/react-query'
import { useMemo } from 'react'
import toast from 'react-hot-toast'
import { useCluster } from '../cluster/cluster-data-access'
import { useAnchorProvider } from '../solana/solana-provider'
import { useTransactionToast } from '../ui/ui-layout'

// this is to link the frontend with the smart contract, ensure it all works
// after this all set up, we can also update the ui in the project ui frontend

// check lib.rs to pass in the info from the validation / struct for this entry
// needed for taking frontend info from user
interface CreateEntryArgs {

  owner: PublicKey,
  title: string,
  message: string,


}

// all the data needed to interact with the program
export function useCrudProgram() {
  const { connection } = useConnection()
  const { cluster } = useCluster()
  const transactionToast = useTransactionToast()
  const provider = useAnchorProvider()
  const programId = useMemo(() => getCrudProgramId(cluster.network as Cluster), [cluster])
  const program = useMemo(() => getCrudProgram(provider, programId), [provider, programId])

  const accounts = useQuery({
    queryKey: ['crud', 'all', { cluster }],
    queryFn: () => program.account.journalEntryState.all(),
  });

  const getProgramAccount = useQuery({
    queryKey: ['get-program-account', { cluster }],
    queryFn: () => connection.getParsedAccountInfo(programId),
  });

  const createEntry = useMutation<string, Error, CreateEntryArgs>({
    mutationKey: ['journalEntry', 'create', { cluster}],
    mutationFn: async ({ owner, title, message}) => {
      return program.methods.createJournalEntry(title, message).rpc();
    },
    onSuccess: (signature) => {
      transactionToast(signature);
      accounts.refetch();
    },
    onError: (error) => {
      toast.error(`Error creating entry: ${error.message}`);
    },
  });

  return {
    program,
    accounts,
    getProgramAccount,
    createEntry,
    programId
  };

}

// in order to update an account that alr exists, we must first derive the PDA and then 
export function useCrudProgramAccount({ account }: { account: PublicKey }) {
  const { cluster } = useCluster()
  const transactionToast = useTransactionToast()
  const { program, accounts } = useCrudProgram()

  // query for an account
  const accountQuery = useQuery({
    queryKey: ['crud', 'fetch', { cluster, account }],
    queryFn: () => program.account.journalEntryState.fetch(account),
  })

  // want to also be able to update an account here
  const updateEntry = useMutation<string, Error, CreateEntryArgs>({

    mutationKey: ['journalEntry', 'update', { cluster }],
    mutationFn: async ({ title, message }) => {
      return program.methods.updateJournalEntry(title, message).rpc(); // we get the params from the smart contract in librs
    },
    onSuccess: (signature) => {
      transactionToast(signature);
      accounts.refetch(); // make sure we update the states of the accounts
    },
    onError: (error) => {
      toast.error(`Error updating entry: ${error.message}`);
    }

  })

  const deleteEntry = useMutation<string, Error>({

    mutationKey: ['journalEntry', 'delete', { cluster }],
    mutationFn: (title: string) => {

      return program.methods.deleteJournalEntry(title).rpc();

    },
    onSuccess: (signature) => {
      transactionToast(signature);
      accounts.refetch();
    },
    onError: (error) => {
      toast.error(`Error deleting entry: ${error.message}`);
    }

  })

  return {
    accountQuery,
    updateEntry,
    deleteEntry
  }

}
