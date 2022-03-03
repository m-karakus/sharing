# Terminal

```python
sudo apt update
sudo apt-get install tilix
sudo update-alternatives --config x-terminal-emulator
echo $SHELL
sudo apt update && sudo apt install zsh
chsh
/bin/zsh
0
cat ~/.zshrc  
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
vim ~/.zshrc 
    # burada plugins=(git) yazısını şununla değiştiriyoruz
    plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

sudo apt install -y fonts-font-awesome
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
vim ~/.zshrc 
    # burada ZSH_THEME="robbyrussell" yazısını şununla değiştiriyoruz
    ZSH_THEME="powerlevel10k/powerlevel10k"
```