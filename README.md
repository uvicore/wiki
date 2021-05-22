# Uvicore Wiki




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


active, disabled
some type of reset_password_code?






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



users can be grouped
roles can be added to a single user, or to a group
permissions are only added to a role

Tables
------
users
groups
roles

user_roles ?? Should we allow this level of granularity? Though we probably must to match with FusionAuth because FA does not give us user groups, only roles?  Or do we match FA roles to Uvicore Groups?  Or what if we want to "ADD" a single role to ONE user already in a group.

user_groups
group_roles
role_permissions



We call "tables" or "models" - entities
We call each row in a table, a record or document

record_group_roles (roles applied to a specific row in database by group)






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

How do we know which ROLES to show for a Post.  Can't show all 100 roles.  Need a `entity_roles` table.  So roles that could be SET for a Post might be Post Viewer, Post Manager only, not other roles like user manager, site manager etc...

entity_roles
id | entity | role
1  | posts  | post_viewer
1  | posts  | post_manager



And there would be a polymorphic table to handle PER record group permissions

**auth_document_group_roles** or auth_record_group_roles
```
 _______________________________________________________
| id | entity    | entity_id  | group_id | role_id      |
|----|-----------|------------|----------|--------------|
| 1  | posts     | 1          | users    | post_viewer  |
| 1  | posts     | 1          | friends  | post_viewer  |
| 1  | posts     | 1          | friends  | post_manager |
|____|___________|____________|__________|______________|
```

maybe another table for `auth_document_user_roles` to apply a role for that document directly to a user also?

So you can see POST #1 any user in the "friends" group is post_viewer and post_manager

Could technically do per user to with a auth_document_user_roles table, but thats pretty fine grained


What about how ERPNext does Sales Person record filters?  You don't "SET" permission on a lead, you use a filter to do it.

auth_entity_group_filters

id | entity | group_id | role         | column       | value
1  | leads  | users    | lead_manager | sales_person | David or $loggedin_user? $me
1  | posts  | users    | post_manager | $me

Notice there is no entity_id as it is not per record, it is for the entire entity where a column matches the value.

So if YOU are the OWNER of post #1, then the `post_manager` role is applied to you.

But what does the filter above do?  Does it give you read or write or both?  Really we want to apply a ROLE if that filter matches.  Thus the ROLE field



And one for users

auth_document_user_filters










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









