# 🔐 GitHub Terminal Authentication Guide

A complete, beginner-friendly guide on how to authenticate your terminal with GitHub on macOS, Linux, and Windows.

---

## 📋 Table of Contents

- [First Step: Configure Your Git Identity](#-first-step-configure-your-git-identity)
- [Method 1: GitHub CLI (`gh auth login`) - Recommended](#-method-1-github-cli-gh-auth-login---recommended)
- [Method 2: SSH Key Setup - Professional Standard](#-method-2-ssh-key-setup---professional-standard)
- [Method 3: HTTPS + Personal Access Token (PAT)](#-method-3-https--personal-access-token-pat)
- [🔍 Troubleshooting & Testing Access](#-troubleshooting--testing-access)

---

## 👤 First Step: Configure Your Git Identity

Before pushing code, tell Git who you are. This name and email will appear on your commit history:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify your config:
```bash
git config --global --list
```

---

## 🚀 Method 1: GitHub CLI (`gh auth login`) - Recommended

The fastest and easiest way to authenticate. It connects your terminal through a browser login.

### 1. Install GitHub CLI:

* **macOS (Homebrew):**
  ```bash
  brew install gh
  ```
* **Windows (winget):**
  ```bash
  winget install --id GitHub.cli
  ```
* **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt install gh
  ```

### 2. Log in:
```bash
gh auth login
```

### 3. Answer the interactive prompts:
1. **What account do you want to log into?** → Select `GitHub.com`
2. **What is your preferred protocol for Git operations?** → Select `SSH` (or `HTTPS`)
3. **Upload your SSH key or generate a new one?** → Select `Generate a new key` (or choose existing)
4. **How would you like to authenticate GitHub CLI?** → Select `Login with a web browser`
5. Press **Enter**, copy the 8-character code, open the browser URL, and approve.

Done! Git credentials are now automatically configured.

---

## 🔑 Method 2: SSH Key Setup - Professional Standard

SSH keys allow passwordless, secure access to GitHub repositories.

### Step 1: Generate an SSH Key
Run this in your terminal (replace with your GitHub email):

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```
* When prompted to *"Enter a file in which to save the key"*, press **Enter** (keeps default path `~/.ssh/id_ed25519`).
* You can optionally enter a passphrase for extra security.

### Step 2: Start SSH Agent and Add Key
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

*(On macOS, to automatically save the passphrase in Apple Keychain, add to `~/.ssh/config`:)*
```text
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

### Step 3: Copy Your Public Key to Clipboard

* **macOS:**
  ```bash
  pbcopy < ~/.ssh/id_ed25519.pub
  ```
* **Linux:**
  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```
* **Windows (Git Bash):**
  ```bash
  clip < ~/.ssh/id_ed25519.pub
  ```

### Step 4: Add Key to GitHub
1. Open [github.com/settings/ssh/new](https://github.com/settings/ssh/new).
2. Enter a **Title** (e.g. `Work Laptop` or `MacBook`).
3. Paste the copied key into the **Key** field.
4. Click **Add SSH key**.

### Step 5: Test Connection
```bash
ssh -T git@github.com
```
Expected output:
```text
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🎫 Method 3: HTTPS + Personal Access Token (PAT)

> ⚠️ **Important:** GitHub does not accept account passwords for terminal operations. You must use a Personal Access Token (PAT).

### Step 1: Create a Personal Access Token on GitHub
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens).
2. Click **Generate new token** → **Generate new token (classic)**.
3. Set **Note**: e.g., `Terminal Token`.
4. Set **Expiration**: e.g., `90 days` or `No expiration`.
5. Select scopes: Check **`repo`** (Full control of private repositories).
6. Click **Generate token**.
7. **Copy the token immediately** (it begins with `ghp_...`). You won't be able to see it again!

### Step 2: Enable Git Credential Helper (saves token so you only enter it once)

* **macOS:**
  ```bash
  git config --global credential.helper osxkeychain
  ```
* **Windows:**
  ```bash
  git config --global credential.helper manager
  ```
* **Linux:**
  ```bash
  git config --global credential.helper store
  ```

### Step 3: Perform a Git Action
When Git asks for credentials during `git clone` or `git push`:
* **Username:** Your GitHub username
* **Password:** Paste your **Personal Access Token (`ghp_...`)**, NOT your account password.

---

## 🔍 Troubleshooting & Testing Access

### 1. Check which remote protocol your repo is using:
```bash
git remote -v
```
* **SSH format:** `git@github.com:vardandanielyan/git-knowledge.git`
* **HTTPS format:** `https://github.com/vardandanielyan/git-knowledge.git`

### 2. Switch between HTTPS and SSH:
* Switch to SSH:
  ```bash
  git remote set-url origin git@github.com:vardandanielyan/git-knowledge.git
  ```
* Switch to HTTPS:
  ```bash
  git remote set-url origin https://github.com/vardandanielyan/git-knowledge.git
  ```

### 3. Check loaded SSH keys:
```bash
ssh-add -l
```

### 4. Test SSH verbose debug output if failing:
```bash
ssh -vT git@github.com
```
