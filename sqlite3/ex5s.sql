select person.first_name, person.last_name from person where age>20;
select pet.id, pet.name from pet where dead=0;
select person.first_name, pet.name from person_pet, person, pet where person_pet.person_id=person.id and person_pet.pet_id=pet.id;