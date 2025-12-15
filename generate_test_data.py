from faker import Faker
import csv
import random

fake = Faker()

def generate_synthetic_users(count=20):
    """Synthetic test data үүсгэх"""
    users = []
    roles = ['Admin', 'User', 'Manager', 'Developer', 'Tester']
    
    for _ in range(count):
        user = {
            'name': fake.name(),
            'email': fake.email(),
            'age': random.randint(18, 65),
            'country': fake.country(),
            'role': random.choice(roles)
        }
        users.append(user)
    
    return users

def save_to_csv(users, filename='test_users.csv'):
    """CSV файл руу хадгалах"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'email', 'age', 'country', 'role'])
        writer.writeheader()
        writer.writerows(users)

if __name__ == '__main__':
    users = generate_synthetic_users(20)
    save_to_csv(users)
    print("✅ 20 synthetic users үүсгэлээ: test_users.csv")
    
    # Эхний 3 хэрэглэгчийг харуулах
    for i, user in enumerate(users[:3], 1):
        print(f"\n{i}. {user['name']}")
        print(f"   Email: {user['email']}")
        print(f"   Age: {user['age']}, Country: {user['country']}, Role: {user['role']}")
