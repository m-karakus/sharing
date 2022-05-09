# Create --bare git repo 
git init --bare $HOME/.dotfiles & alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME' & /
dotfiles config --local status.showUntrackedFiles no & /
echo "alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'" >> $HOME/.zshrc

# push changes
dotfiles status 
dotfiles add .vimrc 
dotfiles commit -m "Add vimrc" 
dotfiles add .bashrc 
dotfiles commit -m "Add bashrc" 
dotfiles push

# Add the bare repo directory to a '.gitignore' file
echo "dotfiles/" >> .gitignore

# clone your repo into a '.dotfiles' directory
git clone --bare <git-repo-url> $HOME/.dotfiles

# Define the alias in the current shell scope:
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# Checkout the actual content from the bare repository to your '$HOME':
dotfiles checkout


# files
dotfiles  add .ssh .cert .config .xmonad .asoundrc .bash_profile .bashrc .p10k.zsh .Xauthority .Xresources .zcompdump-arch-5.8.1 .zshrc 