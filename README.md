# This project is a personal project to learn DDD process

## This project was cloned from [This project](https://github.com/ivanpaulovich/ddd-tdd-rich-domain-model-dojo-kata)

Design the **Virtual Wallet** using Aggregate Roots, Entities and Value Objects and cover the uses cases with Unit Tests. At the Clean Architecture Manga you could learn the [DDD patterns](https://github.com/ivanpaulovich/clean-architecture-manga/wiki/Domain-Driven-Design-Patterns) and TDD at [TheThreeRulesOfTdd](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd).

## :gem: Compiling from source

Clone this repository to your machine, compile and test it:

```sh
git clone https://github.com/arodrigueze0215/virtual-wallet-DDD-practices.git
```

## :construction_worker: Use cases

This project was designed do cover the following use cases and requirements:

1. A Customer could register a new Checking Account using its personal details.
1. Allow a customer to deposit funds into an existing account.
1. Allow the customer to withdraw funds from an existing account.
1. Allow the customer to close a Checking Account only if the balance is zero.
1. Do not allow the Customer to Withdraw more than the existing funds.
1. Allow to get the account details.
1. Allow to get the customer details.

## :memo: The Domain Model

![Domain Model](https://raw.githubusercontent.com/ivanpaulovich/ddd-tdd-rich-domain/kata-initial/docs/ddd-tdd-rich-domain-model.png)

## :computer: Tech stuff

* Python 3.8
* Django 3.1
