# offensive_security
Developing a Recurrent Neural Network to Generate Passwords for Hash-Cracking

Our project is going to use a set of password hashes and a list of brute force cracked passwords, and a recurrent neural network (RNN) to create a list of new potential passwords not contained in the original cracked list. This should also be more effective than a brute-force password generation method, as the neural net will only generate passwords that are similar to the most popular password choices. 
Our plan will proceed in two phases:

## Phase 1:
1.	Use a brute force attack on an existing hash set, generate a list of cracked passwords
2.	Use these cracked passwords to train the RNN
3.	Have the RNN output a new list of passwords
## Phase 2:
1.	Use the generated list of passwords to dictionary attack the hash set
2.	This should result in more passwords being cracked, append these cracked passwords to the cracked password list
3.	Use this larger list to retrain the RNN
4.	The RNN’s output will be a new list of passwords
5.	Feed the RNN’s output into the dictionary attack in Step 1
