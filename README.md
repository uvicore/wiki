auth_users
----------
email
first_name
last_name

phone
website

city
state

country
title


avatar_url


password
disabled
last_login_at
creator_id
created_at
updated_at



auth_groups
-----------
id
name


auth_permissions
----------------
id
name
content_type_id (the table)
codename (add_posts, change_posts, delete_posts, view_posts)

# Uvicore Auth


user=mreschke
group=Employee
table=posts

**auth_users**
```
 ______________________________
| id | email                   |
|----|-------------------------|
| 1  | mreschke@sunfinity.com  |
|______________________________|
```



**auth_roles**
```
 ______________________________________
| id | key           | name            |
|--------------------|-----------------|
| 1  | admin         | Administrator   |
| 2  | post_viewer   | Post Viewer     |
| 3  | post_manager  | Post Manager    |
|____________________|_________________|
```


**auth_groups**
```
 _____________________
| id | name           |
|----|----------------|
| 1  | Administrators |
| 2  | Users          |
| 3  | Family         |
| 4  | Friends        |
|____|________________|
```


Example Post #1 permissions
Show a list of GROUPS and a list of ROLE checkboxes, NOT permissions
```
 _____________________________________________
| Group          | Post Viewer | Post Manager |
|----------------|-------------|--------------|
| Users          | Yes         | No           |
| Friends        | Yes         | Yes          |
|________________|_____________|______________|
```

And there would be a polymorphic table to handle PER record group permissions

**auth_document_group_roles**
```
 _______________________________________________________
| id | entity    | entity_id  | group_id | role_id      |
|----|-----------|------------|----------|--------------|
| 1  | posts     | 1          | users    | post_viewer  |
| 1  | posts     | 1          | friends  | post_viewer  |
| 1  | posts     | 1          | friends  | post_manager |
|____|___________|____________|__________|______________|
```

So you can see POST #1 any user in the "friends" group is post_viewer and post_manager

Could technically do per user to with a auth_document_user_roles table, but thats pretty fine grained











auth_permissions
Permissions are PER entity/table?
=================================
id | table   | perm       |
--------------------------|
1  | posts   | read_posts |



auth_group_permissions
======================
id |
---------------------------
1  |









