# Sea Surfer
      _____               _____             __          
     / ____|             / ____|           / _|         
    | (___   ___  __ _  | (___  _   _ _ __| |_ ___ _ __ 
     \___ \ / _ \/ _` |  \___ \| | | | '__|  _/ _ \ '__|
     ____) |  __/ (_| |  ____) | |_| | |  | ||  __/ |   
    |_____/ \___|\__,_| |_____/ \__,_|_|  |_| \___|_|   

A CSRF PoC generator

Fork me on [GitHub](https://github.com/the-useless-one/sea_surfer).

## HISTORY

I like CSRF vulnerabilities because they are very subtle. I don't think it's
something most developers think of when they develop their web applications,
even people with security notions.

I often have to demonstrate CSRF vulnerabilities during my pentests, and
creating a Proof-of-Concept HTML page is kind of a pain in the ass. So I
decided to create a little Python program to automate this task.

Sea Surfer takes a file containing an HTTP request, and create an HTML page
with a pre-filled form, which will be auto-sent with JavaScript.

It's not the pretitest code, and I'm not the first guy to create something like
that, but here goes, hoping it will be helpful to someone.

## REQUIREMENTS

All you need is Python 3.

## USAGE

Just go to the `sea_surfer` directory and type
the following command:

    ./sea_surfer.py -i <request_file>

where `request_file` is the file where the request used to generate the
Proof-of-Concept is stored.

Don't forget to make the script executable with:

    chmod +x sea_surfer.py

To see a list of the options, just issue:

    ./sea_surfer.py -h
    usage: sea_surfer [-h] -i REQUEST_FILE [-s] [-o OUTPUT_FILE]

    A CSRF PoC generator

    optional arguments:
      -h, --help       show this help message and exit
      -i REQUEST_FILE  file containing the request
      -s               if this flag is set, the form will have an HTTPS action URL
      -o OUTPUT_FILE   HTML output file (default: stdout

### Request file

This file contains the HTTP request from which you want to generate your
Proof-of-Concept HTML file.

### SSL flag

There is no easy way to tell from an HTTP request whether the connection is
made over SSL or not. This flag is used to tell the program whether the form
action URL should starts with `https://` or `http://`.
* If this flag is set, the action URL will starts with `https://`
* If this flag is not set, the program will try to determine from the Referer
header whether the action URL should starts with `https://` or not. If it
can't, it will default to `http://`.

### Output file

This parameter holds the name of the generated HTML file. If no file is
specified, the HTML page will be output to the stdout.

Don't worry about the potential debug messages: they're output to stderr, so
that you can redirect the HTML page from stdout to a file.

## TODO
* Demo mode: for now, the generated HTML PoC is in a form with hidden inputs.
It's stealthier that way, but not very graphic. The demo mode will allow to
generate a demonstrative HTML file, where the form is visible, so as to explain
the vulnerability to someone without prior knowledge.
* Multipart form: for now, only x-www-form-urlencoded POST data are supported.
I plan to support multipart form data in the future.
* Burp plug-in: when I was nearly done coding, a colleague told me that Burp
Pro already does what this program does. I love my colleagues and how they stop
me from wasting my time. So I may do a Burp Plugin for Burp Free.

## COPYRIGHT

Sea Surfer - A CSRF PoC generator

Yannick Méheut [useless (at) utouch (dot) fr] - Copyright © 2015

This program is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the 
Free Software Foundation, either version 3 of the License, or (at your 
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
Public License for more details.

You should have received a copy of the GNU General Public License along 
with this program. If not, see
[http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).

