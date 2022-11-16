Description of algorithm:
Certain seats should be reserved for special needs and they will not be included in the random selection. 
Ask a few questions: Are you in need of consective seats? How many? Why?
If not, then do the random selection
If yes, choose corresponding seats in the reserved sections.


Issues: 
The reserved seats might never get picked and airplane company loses money
People might not be truthful about the reasons why they need consective seats
The price for these pre-selected consective seats can be unfair to some groups
How to include all the legitment reasons? Who will define them?


Collaborator: Elizabeth, Patti, Jenna
## ***My pseudo code for the algorithm:***

When purchasing economy, for each ticket the algorithm is designed to ask:
+ Traveler age on date of travel:
  
  + if 16 years or older:
    + are you traveling with someone 15 years or younger?
      + if yes:
        + allow to be seated together and avoid exit row
  + if 15 years or younger and traveling alone:
    +  allow no exit row
          
  + are you traveling with someone with accessibility needs?
      + if yes:
        + allow to avoid exit row, allow to be seated with group, allow to choose seats based on accessibility needs. 
    
+ Do you have accessibility needs?
  + if yes:
    + allow to avoid exit row and/or allow to be seated with a group member/care giver, allow to choose seat based on accessibility needs.