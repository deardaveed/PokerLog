from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='demo', email='demo@email.com', password='password')
    ivey = User(
        username='ivey', email='ivey@email.com', password='password')
    helmuth = User(
        username='helmuth', email='helmuth@email.com', password='password')
    dwan = User(
        username='dwan', email='dwan@email.com', password='password')
    negreanu = User(
        username='negreanu', email='negreanu@email.com', password='password')

    db.session.add(demo)
    db.session.add(ivey)
    db.session.add(helmuth)
    db.session.add(dwan)
    db.session.add(negreanu)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
