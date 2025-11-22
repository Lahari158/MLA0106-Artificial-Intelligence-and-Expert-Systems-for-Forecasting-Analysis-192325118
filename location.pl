location(hyderabad, telangana).
location(chennai, tamilnadu).
location(mumbai, maharashtra).
location(jaipur, rajasthan).
location(pune, maharashtra).

stays(rahul, hyderabad).
stays(meera, chennai).
stays(aditya, mumbai).
stays(sneha, jaipur).
stays(kiran, pune).
display(Person, City, State) :-
    stays(Person, City),
    location( City, State).

