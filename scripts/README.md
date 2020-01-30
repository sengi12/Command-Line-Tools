# Running Applications from the command line without output to stdout

The reason I do this is because sometimes in Linux, an application you install will be loaded as an `.AppImage` file which isn't able to load in the side bar like other apps. This is a workaround I came up with because I was tired of searching all my apps for it every time I wanted to run it.

#### Linux (Ubuntu)

In this tutorial we will be writing a few scripts that we want to execute from any bash instance. For this we will be editing the previously seen `~/.bashrc` file. We need a place to work so first thing first is that you should create a workspace for your scripts to live like so: `mkdir scripts`. ***(I put this in my Documents folder, but you can put yours anywhere you like.) 

Now we need to edit our `~/.bashrc` file, so open the file in whatever editor you like (vscode, sublime, vim, nano, gedit, etc.) and scroll to the bottom of the file. Add the below line to the bottom of the file. 

> Note how this is my scripts directory location. you will want to replace this with the absolute location on your machine. You can navigate to that location using the `cd` command, and once you are there type `pwd` and it will print the "present working directory" to stdout for you to copy and paste.

```bash
export PATH=/home/sengi/Documents/scripts:$PATH
```

Now time to make our script. For this to work we need an executable to run from the command line. In the below example I'm using "clickup" but any executable app should work. This is the general structure of the command:

```
#!/usr/bin/env bash

nohup path/to/executable/app > /dev/null &
disown
```

- `nohup` allows us to run the app while redirecting the output of the executable elsewhere. By default `nohup` will create a `nohup.out` file, so I redirect it to `/dev/null` so that it gets deleted. 
- `&` gives us the option of running the command in the background.
- `disown` will disconnect the application from the terminal, so that you can close the terminal without completely shutting down the app.

Just for reference, here is the exact script I used for clickup:

```
#!/usr/bin/env bash

nohup /home/sengi/Documents/clickup/app/clickup_x64.AppImage > /dev/null &
disown
```

> *to see more scripts I've written for convenience, check out my scripts folder in this repo*

---

# Opening any file from command line in typora

#### Linux (Ubuntu)

> A version of this script that works with Mac is also in this repo under `scripts/osx/`

Just like many, I love using typora to edit `.md` files. However I would like to easily open a file from the command line so I wrote a script to do just that. The benefit of this script is that it will redirect all the output of the function to `\dev\null` as well as disown it. This way you will see no output to the terminal and you can close the terminal without it closing typora.

How it works:

First it will check to see if the file given exists. If the file already exists, it will open it up in typora. Otherwise, it assumes you are creating a file and will create the file for you in the current working directory, then open it up in typora.

```
#!/usr/bin/env bash
FILE=${1?Error: No file specified. 
            
            Usage: typopen <filename>
            }
if test -f "$FILE"; then
    echo "opening $FILE in typora..."
    nohup typora $FILE > /dev/null &
    disown
else
    echo "creating $FILE in typora..."
    touch $FILE
    nohup typora $FILE > /dev/null &
    disown
fi
```

*to see more scripts I've written for convenience, check out my scripts folder in this repo*

---

