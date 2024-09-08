![1725087951831](image/mid-semestertest/1725087951831.png)

![1725087968257](image/mid-semestertest/1725087968257.png)

# Command

## ALTER

## UPDATE

# Attribute

## simple attribute

cannot be subdivided

## composite attribute

canbe subdivided to yield additional atttributes

![1725167546391](image/mid-semestertest/1725167546391.png)

## single-valued attribute

## multi-valued attribute

![1725167359800](image/mid-semestertest/1725167359800.png)

# Keys

## superkey

superkey uniquely identifers each tuple

## Primary Key

## Foreign Key

## candidate Key

## attribute key

# entity

## Strong entity

got existence-independence(can exist independently)

can exists apart from all of its related entities

has a primary key that uniquely identifies each of its instances.
must have a primary key

example:
![1725170097642](image/mid-semestertest/1725170097642.png)

## Weak entity

A weak entity cannot be uniquely identified by its own attributes alone. Instead, it depends on a strong entity, and its existence is dependent on that strong entity.



# Algebra


### **𝝿 (Pi)** —  **Projection** :

* The **projection** operation is used to select specific columns (attributes) from a relation (table).
* It eliminates duplicates and returns only the specified columns.
  **Example** :
  * **𝝿_{member_name, member_dob}(MEMBER)** : This returns only the `member_name` and `member_dob` columns from the `MEMBER` table.



SENSEI (sensei_id, sensei_name)

TRAINING_SCHEDULE (training_day, training_time, group_id, sensei_id)

ATTENDANCE (training_day, training_time, member_id, attendance_date)

MEMBER (member_id, member_name, member_dob, member_belt, group_id)

GROUP (group_id, group_name, group_age_range)
