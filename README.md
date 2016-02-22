# MCQ project using Django   
 
## Our Requirements :   
  * We have questions and tags ( Taggable Manager )  
  * We need questions who have only a particular tags and exclude those questions which have an extra or less tags  

## Challenges faced before this :   
 * Initially, we were unable to figure out how to achieve this.   
 * How to fetch only those questions which meet our Requirements  
 * You can't actually exclude each tag manually, so you have to pick each and everyone and then filter them out.  
 * If you try to loop on every question and check, then it's not a scalable option  
 * We wanted a more pythonic way that could solve our problem. Though this is not the best one, but still a lot better than our previous ones  

## Focus :   
 * Though this repo has the basic functionality of MCQ, but the focus of this repo is not to create MCQs but to filter out   
   questions with specific tags.  
 * This repo can be used to understand the table structure for designing MCQs and to filter out MCQs from the questions pool.  


## How things work :   
 * We already have a pool of [multiple choice] questions (or we can also add new [multiple choice] questions).  
 * When we create a new contest, we want to filter questions with different tags and add them to the contest pool.  
 * The process of adding [multiple choice] questions to the pool would be following :   
    * The admin specifies the number of questions he/she wants to select and also specify the tags on which they want to filter out questions.  
    * The system tells the number of questions available and ask if they want to add these questions to the contest pool.  
 * Once these question-contest pools are created, questions are then served from these pools to the user randomly .


## Urls : 
 * /contest/create :  create a new contest 
 * /contest/<contest-slug>   : a particular contest 
 * /contest/<contest-slug>/skilltest: skilltest home 
 * /contest/<contest-slug>/skilltest/join : Join skilltest (To be used by candidate)
 * /contest/<contest-slug>/skilltest/mcq/ : MCQ's home
 * /contest/<contest-slug>/skilltest/mcq/<mcq-id>/submit : Submit MCQ's answer
 * /contest/<contest-slug>/skilltest/mcq/<mcq-id>/review : Review MCQ's answer (Shortlist for review)
 * /contest/<contest-slug>/skilltest/mcq/finish : Finish skilltest
 * /mcq/<contest-slug>/create-pool : create contest pool for the particular contest. ( Used by admin  )
 * /mcq/<contest-slug>/save-pool : save contest pool 
 * /mcq/add_multiple : create multiple MCQs from CSV 
 * 
