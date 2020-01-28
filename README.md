# Command-Line-Tools

This repo is dedicated to tools I've found useful on the command line

---

### Create alias for powershell directory command

> I love the layout of the powershell directory command due to how much detailed information you get in the output.

```pwsh
# SAMPLE OUTPUT


    Directory: /Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---         11/15/18  12:15 PM                Documents
d-r---         12/27/18  12:43 AM                Guest
d-----          6/15/19  11:41 AM                user
d-----          3/25/19   9:57 PM                Shared
--rh--          8/17/18   5:56 PM              0 .localized
```

First you'll need PowerShell Core 6.0...

[Microsoft Installation Instructions](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows?view=powershell-6) : This provides instructions to download and install PowerShell Core 6.0 on the following platforms:

- Windows
- Linux
- MacOS
- ARM

---

Once you've installed PowerShell then you need to get familiar with it.

To start a PowerShell terminal you simply type `pwsh` into the command line. You can then exit the terminal with `exit`. 

#### Mac Installation Steps:

- To follow directly along you will need `vim`

```bash
#Mac Vim Installation Instructions
```

- Now to creat our alias. First type in the below command:

```bash
vim ~/.bash_profile
```

> This works on my MacBook. it may not be the case if you are running Windows. I will figure that out soon but for now this is what I got.

- You are now within a vim editor. Press `i` in order to enter INPUT mode within the editor. Now that you can edit the file, add the following line to the top of the file.

```bash
alias l='pwsh -Command "dir -Force"'
```

- NOTE that `l` is simply my preference. You can use anything as your alias for this command.
- Now press the `esc` key to exit INPUT mode. Now that you are not in INPUT mode, enter `:wq`. This will WRITE the changes made, and QUIT the editor.
- Now we have to reload the `.bash-profile` file. simply enter the below line to do this:

```bash
source ~/.bash_profile
```

- Now that the file has been reloaded, you are ready to use the alias! Simply press `l` in any directory to test if it worked properly! 

NOTE that this does take a second to process since you are entering PowerShell, executing a command, and then exiting PowerShell. 

#### Linux (Ubuntu) Installation Steps:

- To follow directly along you will need `vim`

```bash
sudo apt-get install vim
```

- Now to creat our alias. First type in the below command:

```bash
vim ~/.bashrc
```

- You are now within a vim editor. Press `i` in order to enter INPUT mode within the editor. Now that you can edit the file, add the following line to the top of the file.

```bash
alias l='pwsh -Command "dir -Force"'
```

- NOTE that `l` is simply my preference. You can use anything as your alias for this command.
- Now press the `esc` key to exit INPUT mode. Now that you are not in INPUT mode, enter `:wq`. This will WRITE the changes made, and QUIT the editor.
- Now we have to reload the `.bash-profile` file. simply enter the below line to do this:

```bash
source ~/.bashrc
```

- Now that the file has been reloaded, you are ready to use the alias! Simply press `l` in any directory to test if it worked properly! 

NOTE that this does take a second to process since you are entering PowerShell, executing a command, and then exiting PowerShell. 

#### Windows (10) Installation Steps:

> to be continued...

---

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

Just like many, I love using typora to edit `.md` files. However I would like to easily open a file from the command line so I wrote a script to do just that.

```
#!/usr/bin/env bash
FILE=${1?Error: No file specified. 
            
            Usage: typopen <filename>
            }
echo "opening $FILE in typora..."
nohup typora $FILE > /dev/null &
disown
```

*to see more scripts I've written for convenience, check out my scripts folder in this repo*

---

