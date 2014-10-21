select*from pet;
update  pet set name ="Zed's Dead pet" where id in(
select pet.id
from pet, person_pet, person
where
person.id=person_pet.person_id
AND
pet.id=person_pet.pet_id
and
person.first_name="mike"
AND
pet.dead>0
);
select*from pet;