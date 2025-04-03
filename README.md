# Finger_Print_Voting_System

Fingerprint-Based Voting System
This Python script simulates a fingerprint-based electronic voting system. It provides a secure and fair way for voters to cast their votes using unique fingerprint identifiers. The system ensures that each voter can vote only once and that votes are counted accurately.

Key Features
✔ Candidate Registration – Admins can register candidates before the election starts.
✔ Voter Registration – Voters must register with a unique fingerprint ID (simulated as user input).
✔ Secure Authentication – Voters are verified using a hashed fingerprint ID before voting.
✔ One-Person, One-Vote – Prevents multiple votes from the same voter.
✔ Election Control – Admins can start and stop the election as needed.
✔ Live Vote Counting – Results can be displayed at any time.
✔ Voter Status Tracking – Shows whether a voter has cast their vote or not.

How It Works
1️⃣ Register Candidates – Admins add candidates before starting the election.
2️⃣ Register Voters – Each voter must register using their name and a unique fingerprint identifier.
3️⃣ Start the Election – Voting is only possible when the election is active.
4️⃣ Authenticate & Vote – Voters provide their fingerprint ID to cast a vote.
5️⃣ Stop Election & Display Results – Admins can stop voting and view the election results.

Technologies Used
🟢 Python – Core programming language
🟢 Hashing (SHA-256) – Used to securely store fingerprint IDs
🟢 Command-Line Interface – Interactive user experience

This system is a simulation and does not use actual fingerprint scanning hardware. Instead, unique identifiers are used to represent fingerprints.
