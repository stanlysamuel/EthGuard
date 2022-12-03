// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as cp from "child_process";

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('ethguard.helloWorld', async () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		const editor = vscode.window.activeTextEditor?.document.fileName;
		// editor.document.save();

		const execShell = (cmd: string) =>
			new Promise<string>((resolve, reject) => {
				cp.exec(cmd, (err, out) => {
					if (err) {
						return reject(err);
					}
					return resolve(out);
				});
    	});
		const result = await execShell('python3 /Users/stanly/Project/Veridise/redetector/code/peculiar_dummy.py ' + editor);
		vscode.window.showInformationMessage(result);
	});

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {}
