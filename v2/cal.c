#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    if (strcmp(argv[1], "--help") == 0) {
        fprintf(stderr,
                "usage: cal [--help] [--force]\n"
                "<command> [<args>]\n\n"

                "These are common Cal commands used in various situations:\n\n"

                "start a working area\n"
                "  init      Initialize a repository to act as your project folder\n\n"

                "setup Autograder compatibility\n"
                "  setup     Set up Autograder for a project repository\n\n"

                "submit your project to Autograder\n"
                "  submit    Submit the designated project file/package in your project repository\n\n"

                "check the status of your projects\n"
                "  status    Check submission status of all current projects\n\n"

                "See cal help <command> to read about a specific command\n"
            );
        return 0;
    }

    // sets up cal autograder
    else if (strcmp(argv[1], "setup") == 0) {
        fprintf(stderr, "setting up...\n");
        char *password = getpass("Password: ");
        fprintf(stderr, "%s\n", password);
        return 0;
    }

    // submits file to autograder
    else if (strcmp(argv[1], "submit") == 0) {
        // call with filename parameter
        if (argc == 3) {
            fprintf(stderr, "submitting project...\n");
        }
        else {
            fprintf(stderr, "no filename specified\ntype cal --help for more details");
        }
        return 0;
    }

    // checks status of all projects
    else if (strcmp(argv[1], "status") == 0) {
        fprintf(stderr, "checking...\n");
        return 0;
    }
}
