# EthGuard: Responsive ML based Smart Contract Vulnerability Detection for VSCode

EthGuard is a VSCode extension that uses a pre-trained ML model to predict the possibility of four types of common bugs in Solidity Smart Contracts:
* Re-entrancy
* Front runner
* Access Control
* Unchecked low calls

The extension is automatically invoked when VSCode is initialized and runs the classifier for each of these bugs upon every save. This aids developers in predicting if they are writing sound code. Since we are using an ML model, we are neither guaranteed to be sound nor complete. However, our experimentation proves that 73% to 97% accuracy depending on the type of bug we are trying to detect.

This is a competition entry for Ethereum India Hackathon 2022.

## Motivation

Smart contracts are widely used in the blockchain space for multi-party transactions that involve monetary exchange. However, these contracts are prone to security vulnerabilities that has cost more than 2.1B dollars in the last year itself.
Current manual and automatic approaches/ tools range from a low level expertise to high level expertise in terms of skills and also vary in terms of scalability depending on the complexity of the approach.
However, these require the user to submit the code externally for checks whereas it is obvious that the most natural and ideal way for such checks is to enable the coder right within their development environment (for example as a VSCode extension). However, most of these tools are not tractable enough for quick detection of bugs and hence such an extension is a far fetched goal.
Thus, we focus on an efficient and responsive VSCode plugin, enabled due to machine learning, to help developers catch well known bugs at runtime. We train an existing model to 
* VSCode extension
* Tested on 3 more bugs
* Improved performance of existing re-entrancy detector using  ABalanced dataset

<!-- ## Results
TODO

## Features

Describe specific features of your extension including screenshots of your extension in action. Image paths are relative to this README file.

For example if there is an image subfolder under your extension project workspace:

\!\[feature X\]\(images/feature-x.png\)

> Tip: Many popular extensions utilize animations. This is an excellent way to show off your extension! We recommend short, focused animations that are easy to follow.

## Requirements

If you have any requirements or dependencies, add a section describing those and how to install and configure them. -->

## Extension Settings
TODO
<!-- Include if your extension adds any VS Code settings through the `contributes.configuration` extension point.

For example:

This extension contributes the following settings:

* `myExtension.enable`: Enable/disable this extension.
* `myExtension.thing`: Set to `blah` to do something. -->

## Known Issues

We hard code the path in line 27 of `src/extension.ts`. This will have to be manually changed upon reinstalling.

## Release Notes

### 1.0.0

Initial release of EthGuard which is an ML based Smart Contract Vulnerability Detection for VSCode. We support the following bugs:
* Re-entrancy
* Front runner
* Access Control
* Unchecked low calls

## Members

- Ajinkya Rajput, Veridise Inc. and Indian Institute of Science, Bangalore
- Stanly Samuel, Veridise Inc. and Indian Institute of Science, Bangalore
- Himanshu Vashisht, Veridise Inc.

## Challenges we ran into

Obtaining the dataset was a challenge. Although the Smart Bugs dataset was present, we had to extract relevant datasets from them for the different classes of bugs that we consider.

Large model sizes were difficult to deal with due to limited internet connectivity. Hence, it was time consuming.

VSCode extension documentation is very sparse. Information is easily available for callbacks pertaining to the initialization of extensions. However, it was challenging to figure out the right API's to use to analyse code at runtime in VSCode.
