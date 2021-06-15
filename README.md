# shopping-cart
Project for summer 2021 Intro to Python class
A Python application to modernize the checkout system of a local grocer.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.8+
  + Pip
  + Python-dotenv

## Installation

Fork this z`[remote repository] (https://github.com/mdv5/shopping-cart.git) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-cart":

```sh
conda create -n shopping-cart python=3.8
conda activate shopping-cart
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify the following environment variables:

TAX_RATE = ENTER LOCAL TAX RATE HERE

## Usage

Run the shopping-cart script:

```py
python shopping_cart.py
```

## General app rules
Follow the prompts to input the product id for each item you would like to add to the cart. The app will only allow valid product ids. When you are done entering products. Type 'done' to complete the transaction and print the receipt.
