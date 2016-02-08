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
