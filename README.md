# CAL
Contributers: [Nick Brown](https://github.com/bicknrown) [Emil Kovacev](https://github.com/emilcovacev) [Adam Russell](https://github.com/russella26) [Jake Savitt](https://github.com/jakesavi)

## PLAN
We plan to create an easily-installable CLI used to set progress frameworks on files, and manage directories as projects/assignments. We also intend on integrating command-line access to UB's expanded Autolab submission system, so that students can submit their assignments via the command line

## STEPS
1. Design the interface (pre-hackathon)
2. Test a simple python package (prints filename/date)
3. Create a system to assign due dates to files
4. Add functionality to embed a workflow in the command-line
5. Add functionality to call workflow and file information from the command-line
6. Add functionality to designate directories as projects with a due date and a workflow
7. Add functionality to interact with Autolab API

## CHECKLIST
1. Label files with due dates
2. Label directories as projects
3. Functionality to set workflow for projects
4. Display projects (by due date/title) → check to see if a project is due soon
5. Integration with Autolab API
   1. Submit project to autograder
   2. Recognize submission file
   3. Throw warnings if student did not follow proper precautions (to prevent student from wasting submissions)
   4. Prevent student from submitting if the file type doesn't match autograder submission (if possible)
6. Set advanced workflows for projects
7. multi-step processes
8. priorities
9. branched workflows

## RESOURCES
* [Master Tutorial](https://packaging.ubuntu.com/html/packaging-new-software.html)
* [How to package with Debian](https://wiki.debian.org/Packaging/Intro?action=show&redirect=IntroDebianPackaging)
* [Python "Build Distribution" Docs](https://docs.python.org/3.1/distutils/builtdist.html)
* [Autolab API Overview](https://docs.autolabproject.com/api-overview/)
