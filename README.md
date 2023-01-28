# CryptThemAll

![project category](https://img.shields.io/badge/Project%20Category-DN-red?style=flat-square)
![project version](https://img.shields.io/badge/Version-DN-brightgreen?style=flat-square)
![what-else?](https://img.shields.io/badge/What%20else-DN-blue?style=flat-square)

## About

### Project

An easy-to-use tool to encrypt your personal files.  
Comes with a large choice of encryption algorithms :
...  
(TO DO)

### Author

This tool was made by Ryo Deyn.

## Getting Started

### Requirements

It is necessary to have Python (version 3.10 or higher) installed.
Download link : https://www.python.org/downloads/

(TO DO)

### Installation

(TO DO)

## Usage

(DRAFT)

In a terminal :
```
python lets_crypt.py [OPTIONS] [TARGET]
```
OPTIONS :
```
   -d (or --decrypt)                  to decrypt the specified target. Be aware of using the same
                                      algorithm you used for encryption.
                                      
   -a (or --algorithm) <algo_code>    to specify the wanted algorithm for encryption. See 'Algo Codes'
                                      section below for possible algorithms.
                                      
   -? (TO DEFINE)                     needed informations to encrypt.
   
   -k (or --keep)                     keeps the original file intact and encrypts its content into a
                                      copy.
                                      
   -v (or --version)                  display the current version of the program.
   
   -h (or --help)                     display the possible options.
``` 
TARGET :
```
   file_name                          the name of the file to encrypt (or decrypt).
   | dir_name                         the name of the directory to encrypt (or decrypt).
```
Algo Codes :
```
There are two possible types of encryption algorithms:
   
   - Symmetric-key algorithm:
       codes = {aes, twofish, idea}
           aes -> (TO DEFINE)
           twofish -> (TO DEFINE)
           idea -> (TO DEFINE)
           
   - Asymmetric-key algorithm:
       codes = {rsa, ecc}
           rsa -> (TO DEFINE)
           ecc -> (TO DEFINE)
```
#### Demonstration :

(TO DO)

## Roadmap :

(TO DO)

## License

This project is licensed under the Mozilla Public License 2.0 .
