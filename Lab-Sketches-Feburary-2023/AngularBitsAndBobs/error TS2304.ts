/* 
🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡

                                                █▀▀ █▀█ █▀█ █▀█ █▀█   ▀█▀ █▀ ▀█ █▀█ █░█
                                                ██▄ █▀▄ █▀▄ █▄█ █▀▄   ░█░ ▄█ █▄ █▄█ ▀▀█

                                                      ░░██▓▓░░░░░░░░░░░░░░▓▓▓▓░░                    
                                                    ░░▓▓▒▒▓▓████▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒                  
                                                    ▓▓▒▒▒▒████▒▒▒▒▒▒▒▒▒▒████▓▓▒▒▒▒▒▒                
                                                    ▓▓▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▒▒▒▒                
                                                    ▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒                
                                                  ▒▒██▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒██▓▓                  
                                                    ▓▓▓▓▓▓▒▒▒▒░░    ▒▒▒▒  ▒▒▒▒▓▓▒▒▒▒                
                                                    ▒▒▒▒██▒▒░░██      ▒▒░░  ▒▒▒▒▒▒▓▓                
                                                    ▒▒▒▒▒▒▒▒  ██      ▒▒░░  ▓▓▒▒▒▒▓▓                
                                                    ▓▓▒▒▒▒▓▓░░░░░░  ░░░░░░▓▓▒▒▒▒▓▓░░                
                                                    ░░▒▒▒▒▒▒░░░░██▒▒██▒▒░░  ▓▓▒▒▓▓                  
                                                    ▒▒▓▓▒▒▒▒  ██▓▓▓▓▒▒██░░  ▓▓▒▒▓▓                  
                                                      ▒▒▓▓▓▓░░██░░▓▓▒▒▒▒░░██▒▒▒▒                    
                                                      ▒▒▓▓▒▒  ░░██████▓▓  ░░▓▓▓▓                    
                                                        ██                  ▒▒                      

The error TS2304: Cannot find name 'prompt' occurs in TypeScript when the TypeScript compiler is unable to find the declaration for the prompt 
function. This error occurs because the prompt function is not part of the TypeScript language and is only available in web browsers.

To resolve this error, you need to either declare the prompt function yourself or include a TypeScript definition file that provides a 
declaration for prompt. You can declare the prompt function using the following code:

typescript

declare const prompt: (message?: string) => string;

This will tell the TypeScript compiler that the prompt function exists, and it will not throw the TS2304 error. 
However, keep in mind that you will still need to run your code in a web browser to actually use the prompt function.

date 2/9/23


                                        █░█░█ █▀█ █▀█ █▄▀ ▄▀█ █▀█ █▀█ █░█ █▄░█ █▀▄ ░░▄▀ █▀▀ █ ▀▄▀
                                        ▀▄▀▄▀ █▄█ █▀▄ █░█ █▀█ █▀▄ █▄█ █▄█ █░▀█ █▄▀ ▄▀░░ █▀░ █ █░█

                              declare var prompt: (message?: string, defaultValue?: string) => string;


🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡 🅔🅡🅡🅞🅡🅡
*/

const r = prompt(`Enter the response >`) // the following code will cause an exception!