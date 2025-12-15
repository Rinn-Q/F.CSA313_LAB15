# LOGIN FUNCTIONALITY - TEST CASES

**Feature:** User Login
**Created:** 2025-12-15
**Author:** Жавхлан.Э (B222270051)

---

## 1. FUNCTIONAL TEST CASES

### TC001: Valid Login with Correct Credentials
**Priority:** High  
**Type:** Positive

| Field | Value |
|-------|-------|
| **Preconditions** | User is registered in the system |
| **Test Data** | Email: `user@example.com`<br>Password: `ValidPass123!` |

**Steps:**
1. Navigate to login page
2. Enter valid email address
3. Enter valid password
4. Click "Login" button

**Expected Result:**
- ✅ User is redirected to Dashboard
- ✅ Welcome message displays user's name
- ✅ Session token is created

---

### TC002: Login with Valid Email, Invalid Password
**Priority:** High  
**Type:** Negative

**Steps:**
1. Navigate to login page
2. Enter valid email: `user@example.com`
3. Enter invalid password: `WrongPass123`
4. Click "Login" button

**Expected Result:**
- ❌ Error message: "Invalid email or password"
- ❌ User remains on login page
- ❌ Password field is cleared

---

## 2. BOUNDARY TEST CASES

### TC003: Account Lockout After 3 Failed Attempts
**Priority:** Critical  
**Type:** Security

**Steps:**
1. Enter valid email
2. Enter wrong password - Attempt 1
3. Click Login → See error
4. Enter wrong password - Attempt 2
5. Click Login → See error
6. Enter wrong password - Attempt 3
7. Click Login

**Expected Result:**
- ⚠️ After 3rd attempt: "Account temporarily locked. Try again in 15 minutes"
- 🔒 Account is locked for 15 minutes
- 📧 Email notification sent to user

---

### TC004: Empty Email Field
**Priority:** Medium  
**Type:** Validation

**Steps:**
1. Leave email field empty
2. Enter valid password
3. Click "Login" button

**Expected Result:**
- ⚠️ Validation error: "Email is required"
- 🔴 Email field highlighted in red
- ❌ Form is not submitted

---

### TC005: Empty Password Field
**Priority:** Medium  
**Type:** Validation

**Steps:**
1. Enter valid email
2. Leave password field empty
3. Click "Login" button

**Expected Result:**
- ⚠️ Validation error: "Password is required"
- 🔴 Password field highlighted in red

---

## 3. UI/UX TEST CASES

### TC006: Password Visibility Toggle
**Priority:** Medium  
**Type:** Functional

**Steps:**
1. Enter password in password field
2. Verify password is masked (••••••)
3. Click "Show Password" icon (👁️)
4. Verify password is visible
5. Click "Hide Password" icon
6. Verify password is masked again

**Expected Result:**
- ✅ Toggle works correctly
- ✅ Icon changes between 👁️ and 👁️‍🗨️
- ✅ Password visibility changes

---

## 4. SECURITY TEST CASES

### TC007: SQL Injection Attempt
**Priority:** Critical  
**Type:** Security

**Test Data:**
```
Email: admin' OR '1'='1 Password: anything
```
**Expected Result:**
- ✅ Input is sanitized
- ❌ Login fails with "Invalid credentials"
- 🚫 No SQL error exposed

---

### TC008: XSS Attack Prevention
**Priority:** Critical  
**Type:** Security

**Test Data:**
```
Email: <script>alert('XSS')</script>@test.com Password: test123
```
**Expected Result:**
- ✅ Script tags are escaped
- ❌ No JavaScript execution
- ⚠️ Validation error for invalid email format

---

## 5. EDGE CASES

### TC009: Very Long Email (>255 characters)
**Priority:** Low  
**Type:** Boundary

**Test Data:**
```
Email: aaaaaaaaaa...@example.com (300 characters)
```
**Expected Result:**
- ⚠️ Error: "Email must be less than 255 characters"
- OR
- ✅ Input is truncated at 255 characters

---

### TC010: Special Characters in Password
**Priority:** Medium  
**Type:** Positive

**Test Data:**
```
Password: P@$$w0rd!#%&*()
```
**Expected Result:**
- ✅ Special characters are accepted
- ✅ Login succeeds if credentials are valid

---

## 6. PERFORMANCE TEST CASES

### TC011: Login Response Time
**Priority:** Medium  
**Type:** Performance

**Steps:**
1. Enter valid credentials
2. Click Login
3. Measure time until Dashboard loads

**Expected Result:**
- ⏱️ Response time < 2 seconds
- ✅ No timeout errors

---

## TEST SUMMARY

| Category | Total | Passed | Failed | Blocked |
|----------|-------|--------|--------|---------|
| Functional | 2 | - | - | - |
| Boundary | 3 | - | - | - |
| UI/UX | 1 | - | - | - |
| Security | 2 | - | - | - |
| Edge Cases | 2 | - | - | - |
| Performance | 1 | - | - | - |
| **TOTAL** | **11** | **0** | **0** | **0** |

---

## NOTES

- 🔴 High Priority: TC001, TC002, TC003, TC007, TC008
- 🟡 Medium Priority: TC004, TC005, TC006, TC010, TC011
- 🟢 Low Priority: TC009

**Last Updated:** 2025-12-15
