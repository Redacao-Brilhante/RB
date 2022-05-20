from models.user.role import Role, Permission

# permissions
update_user_profile = Permission(name="update user profile", description="update user profile")
remove_user = Permission(name="remove user", description="remove user")

send_essay = Permission(name="send essay", description="send essay")
delete_essay = Permission(name="delete essay", description="delete essay")
evaluate_essay = Permission(name="evaluate essay", description="evaluate users' essays")

# roles
student = Role(
    name="student",
    slug="student",
    permissions=[
        update_user_profile,
        send_essay,
        delete_essay,
    ]
)

teacher = Role(
    name="teacher",
    slug="teacher",
    permissions=[
        update_user_profile,
        evaluate_essay
    ]
)

admin = Role(
    name="admin",
    slug="admin",
    permissions=[
        update_user_profile,
        remove_user,
        send_essay,
        delete_essay,
        evaluate_essay
    ]
)
