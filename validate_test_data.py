import csv
from collections import Counter

def validate_test_data(filename='test_users.csv'):
    """Synthetic data-н чанар шалгах"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        users = list(reader)
    
    print("=" * 60)
    print("📊 SYNTHETIC DATA VALIDATION REPORT")
    print("=" * 60)
    
    # 1. Нийт мөр
    print(f"\n✅ Нийт мөр: {len(users)}")
    
    # 2. Давхардал шалгах
    emails = [u['email'] for u in users]
    email_counts = Counter(emails)
    duplicates = [email for email, count in email_counts.items() if count > 1]
    
    if duplicates:
        print(f"⚠️  Давхардсан имэйл: {len(duplicates)}")
        for email in duplicates:
            print(f"   - {email}")
    else:
        print(f"✅ Давхардсан имэйл: 0")
    
    # 3. Нас шалгах
    invalid_ages = []
    for u in users:
        age = int(u['age'])
        if not (18 <= age <= 65):
            invalid_ages.append(f"{u['name']} (Age: {age})")
    
    if invalid_ages:
        print(f"\n⚠️  Буруу нас (18-65 бус): {len(invalid_ages)}")
        for item in invalid_ages:
            print(f"   - {item}")
    else:
        print(f"✅ Буруу нас: 0")
    
    # 4. Хоосон утга шалгах
    empty_fields = []
    for i, u in enumerate(users, 1):
        for field, value in u.items():
            if not value or value.strip() == '':
                empty_fields.append(f"Row {i}, Field: {field}")
    
    if empty_fields:
        print(f"\n⚠️  Хоосон утга: {len(empty_fields)}")
        for item in empty_fields[:5]:  # Эхний 5-ыг харуулах
            print(f"   - {item}")
    else:
        print(f"✅ Хоосон утга: 0")
    
    # 5. Role distribution
    roles = [u['role'] for u in users]
    role_counts = Counter(roles)
    print(f"\n📈 Role хуваарилалт:")
    for role, count in role_counts.most_common():
        percentage = (count / len(users)) * 100
        print(f"   {role}: {count} ({percentage:.1f}%)")
    
    # 6. Email domain шалгах
    domains = [email.split('@')[1] for email in emails]
    domain_counts = Counter(domains)
    print(f"\n📧 Email domain-ууд:")
    for domain, count in domain_counts.most_common(5):
        print(f"   {domain}: {count}")
    
    # 7. PII шалгах (энгийн шалгалт)
    pii_keywords = ['real', 'actual', 'personal', 'ssn', 'passport']
    pii_found = []
    
    for u in users:
        user_str = str(u).lower()
        for keyword in pii_keywords:
            if keyword in user_str:
                pii_found.append(f"{u['name']} contains '{keyword}'")
    
    if pii_found:
        print(f"\n⚠️  PII асуудал: {len(pii_found)}")
        for item in pii_found[:3]:
            print(f"   - {item}")
    else:
        print(f"\n✅ PII олдсонгүй")
    
    # 8. Дүгнэлт
    print("\n" + "=" * 60)
    total_issues = len(duplicates) + len(invalid_ages) + len(empty_fields) + len(pii_found)
    
    if total_issues == 0:
        print("🎉 ДҮГНЭЛТ: Өгөгдлийн чанар МАШ САЙН!")
    elif total_issues <= 3:
        print("✅ ДҮГНЭЛТ: Өгөгдлийн чанар САЙН (бага зэрэг асуудал)")
    else:
        print("⚠️  ДҮГНЭЛТ: Өгөгдлийн чанар САЙЖРУУЛАХ ШААРДЛАГАТАЙ")
    
    print("=" * 60)

if __name__ == '__main__':
    validate_test_data()
