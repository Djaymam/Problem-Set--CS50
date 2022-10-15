-- Keep a log of any SQL queries you execute as you solve the mystery.
select * from crime_scene_reports;
select * from crime_scene_reports where id = 295;  --the duck steal
select * from interviews where year=2020;--checking the withesses
select * from interviews where year=2020 and month = 7;
select * from interviews where transcript like '%courthouse%';
select * from interviews where transcript like '%courthouse%' and month=7;--finding the right transcript
select DISTINCT * from courthouse_security_logs where year = 2020 and month=7;--security camera log 
select * from atm_transactions where year=2020 and month=7;
select * from atm_transactions where month=7 and atm_location='Fifer Street';

select * from people join bank_accounts on bank_accounts.person_id=people.id where account_number= 28500762; --THIS AND ALL ACCT NUMBER THAT USE ATM IN FIFER STREET

SELECT * from phone_calls; ---chceck the phone call of the suspects
select * from phone_calls where day=28 and duration<60--the withesses said that the thief talk less than 1min 

select * from flights;--check the flight on the day afther the robery
select * from flights where day=29 and hour<10;--the withesses said they would filght early in morning

select * from airports where id=8; --checking the name of the airports
select * from airports where id=4;
select * from airports where id=1;

select * from passengers join flights on flights.id=passengers.flight_id where flights.id=36; ----checking all passengers on the fligths that day early
select * from passengers join flights on flights.id=passengers.flight_id where flights.id=43;



select * from people where phone_number='(375) 555-8161';--checking the ACCOMPLICE

