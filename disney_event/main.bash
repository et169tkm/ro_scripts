#!/bin/bash

# print traces for debug use
#set -o xtrace

# The encrypred file containing the facebook username and passwords
PASSWORD_FILE_PATH='../private/facebook_password.aes-256-ctr.pbkdf2.enc'

# Asks for the password to decrypt the file, then decrypt the file, and print to stdout
#
# The file is expected to be generated with the following command:
# openssl enc -aes-256-ctr -in <plaintext_file> -out <encrypted_file> -pbkdf2
# 
# The plaintext is expected to contain the credentials of one account per line
# Each line is in the format "<display_name> <username> <password>"
function decrypt_password_file() {
  local path="$1"
  local password=""
  read -s -p "Password for decrypting: " 'password'
  echo "$password"

  echo "$password" | \
    openssl enc \
      -d \
      -aes-256-ctr \
      -in "$path" \
      -pbkdf2 \
      -pass stdin
}

function run_webdriver() {
  local credentials=$( decrypt_password_file "$PASSWORD_FILE_PATH" | awk 'NF==3{print $0}' )
  local credentials_count=$( echo "$credentials" | wc -l )

  local i
  for i in $( seq 1 "$credentials_count" ); do
    local line=$( echo "$credentials" | head -n $i | tail -n 1 )
    local username=$( echo "$line" | awk '{print $2}' )
    local password=$( echo "$line" | awk '{print $3}' )

    echo "Running webdriver on ${username}" >&2
    echo "$password" | python3 webdriver_ro_disney.py --stdin_password "$username"
  done
}

run_webdriver
