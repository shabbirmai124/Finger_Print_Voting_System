import hashlib
import time
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

class Voter:
    def __init__(self, voter_id, name, fingerprint_id_hash):
        self.voter_id = voter_id
        self.name = name
        self.fingerprint_id_hash = fingerprint_id_hash
        self.has_voted = False

    def __str__(self):
        return f"ID: {self.voter_id}, Name: {self.name}, Has Voted: {self.has_voted}"

class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name
        self.vote_count = 0

    def __str__(self):
        return f"ID: {self.candidate_id}, Name: {self.name}, Votes: {self.vote_count}"

class VotingMachine:
    def __init__(self):
        self.registered_voters = {}
        self.candidates = {}
        self.election_active = False
        self._next_voter_reg_id = 1
        self._next_candidate_id = 1

    def add_candidate(self, name):
        if self.election_active:
            print("Cannot add candidates while the election is active.")
            return None
        for existing_candidate in self.candidates.values():
            if existing_candidate.name.lower() == name.lower():
                print(f"Error: Candidate '{name}' already exists.")
                return None
        candidate_id = self._next_candidate_id
        candidate = Candidate(candidate_id, name)
        self.candidates[candidate_id] = candidate
        self._next_candidate_id += 1
        print(f"Candidate '{name}' added successfully with ID {candidate_id}.")
        return candidate

    def register_voter(self, name, fingerprint_id):
        if self.election_active:
            print("Cannot register new voters while the election is active.")
            return False
        if not fingerprint_id:
            print("Error: Fingerprint ID cannot be empty.")
            return False
        fingerprint_id_hash = hash_data(fingerprint_id)
        if fingerprint_id_hash in self.registered_voters:
            print(f"Error: This fingerprint (ID: {fingerprint_id}) is already registered.")
            print(f"Registered to: {self.registered_voters[fingerprint_id_hash].name}")
            return False
        voter_id = self._next_voter_reg_id
        voter = Voter(voter_id, name, fingerprint_id_hash)
        self.registered_voters[fingerprint_id_hash] = voter
        self._next_voter_reg_id += 1
        print(f"Voter '{name}' registered successfully (Reg ID: {voter_id}).")
        return True

    def start_election(self):
        if not self.candidates:
            print("Cannot start election: No candidates have been added.")
            return False
        if not self.registered_voters:
            print("Cannot start election: No voters have been registered.")
            return False
        print("\n--- Election Started ---")
        self.election_active = True
        return True

    def stop_election(self):
        print("\n--- Election Stopped ---")
        self.election_active = False

    def authenticate_voter(self, provided_fingerprint_id):
        if not self.election_active:
            print("Election is not currently active.")
            return None
        provided_fingerprint_hash = hash_data(provided_fingerprint_id)
        voter = self.registered_voters.get(provided_fingerprint_hash)
        if voter is None:
            print("Authentication Failed: Fingerprint not recognized.")
            return None
        if voter.has_voted:
            print(f"Authentication Failed: Voter {voter.name} (ID: {voter.voter_id}) has already voted.")
            return None
        print(f"Authentication Successful: Welcome {voter.name} (ID: {voter.voter_id}).")
        return voter

    def cast_vote(self):
        if not self.election_active:
            print("Voting is currently closed.")
            return
        if not self.candidates:
            print("No candidates are available to vote for.")
            return
        print("\n--- Cast Your Vote ---")
        fingerprint_id = input("Please enter your unique Fingerprint ID: ")
        voter = self.authenticate_voter(fingerprint_id)
        if voter:
            print("\nPlease choose a candidate:")
            candidate_list = list(self.candidates.values())
            for i, candidate in enumerate(candidate_list):
                print(f"{i + 1}. {candidate.name}")
            while True:
                try:
                    choice_num = int(input(f"Enter the number (1-{len(candidate_list)}) of your chosen candidate: "))
                    if 1 <= choice_num <= len(candidate_list):
                        chosen_candidate_obj = candidate_list[choice_num - 1]
                        break
                    else:
                        print("Invalid choice number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            chosen_candidate_obj.vote_count += 1
            voter.has_voted = True
            print("\nVote successfully cast for:", chosen_candidate_obj.name)
            time.sleep(2)

    def display_results(self):
        print("\n--- Election Results ---")
        total_votes = sum(c.vote_count for c in self.candidates.values())
        print(f"Total Votes Cast: {total_votes}\n")
        sorted_candidates = sorted(self.candidates.values(), key=lambda c: c.vote_count, reverse=True)
        for candidate in sorted_candidates:
            print(f"- {candidate.name}: {candidate.vote_count} votes")

    def display_voter_status(self):
        print("\n--- Registered Voter Status ---")
        for voter in self.registered_voters.values():
            status = "Voted" if voter.has_voted else "Not Voted"
            print(f"- {voter.name} (Reg ID: {voter.voter_id}): {status}")


def main_menu(machine):
    while True:
        clear_screen()
        print("\n===== Simulated Fingerprint Voting System =====")
        print("1. Add Candidate")
        print("2. Register Voter")
        print("3. Start Election")
        print("4. Cast Vote")
        print("5. Stop Election")
        print("6. Display Election Results")
        print("7. Display Voter Status")
        print("8. Exit")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            continue
        clear_screen()
        if choice == 1:
            machine.add_candidate(input("Enter candidate name: "))
        elif choice == 2:
            machine.register_voter(input("Enter voter's full name: "), input("Enter Fingerprint ID: "))
        elif choice == 3:
            machine.start_election()
        elif choice == 4:
            machine.cast_vote()
        elif choice == 5:
            machine.stop_election()
        elif choice == 6:
            machine.display_results()
        elif choice == 7:
            machine.display_voter_status()
        elif choice == 8:
            break

if __name__ == "__main__":
    main_menu(VotingMachine())
