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
