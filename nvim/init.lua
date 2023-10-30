require("myconf")

vim.cmd([[
  set guicursor=""
  set nu
  set relativenumber
  set tabstop=4
  set softtabstop=4
  set shiftwidth=4
  set expandtab
  set clipboard=unnamedplus
  set termguicolors
  set smartindent
  set scrolloff=8
  set undofile
  set undodir="~/.vim/undodir"
  set incsearch
  set nohls
  set signcolumn
  set colorcolumn="80"
  set cursorline
  set cursorcolumn
  set autoread
  set updatetime=50
  colorscheme habamax
  hi Normal guibg=NONE ctermbg=NONE
  set foldmethod=indent
  set foldnestmax=10
  set foldlevel=5
  set foldenable
  filetype on
  filetype plugin on
  filetype indent on
  set showmode
  set showmatch
  set showcmd
  set history=1000
  set wildmenu
  set wildmode=list:longest
  set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx
  ]])
