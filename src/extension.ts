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
	vscode.window.showInformationMessage("EthGuard is running in the background ... ");
	let disposable = 
		vscode.workspace.onDidSaveTextDocument( async () => {
			const editor = vscode.window.activeTextEditor?.document.fileName;
			const execShell = (cmd: string) =>
			new Promise<string>((resolve, reject) => {
				cp.exec(cmd, (err, out) => {
					if (err) {
						return reject(err);
					}
					return resolve(out);
				});
    		});
			vscode.window.showInformationMessage("Analysing code upon save ...");
			const result = await execShell('python3 /Users/stanly/Project/Veridise/ethguard/src/detectors/dummy_detector.py ' + editor);
			vscode.window.showInformationMessage(result);
		});

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {}
