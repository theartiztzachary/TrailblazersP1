#Test Strategy Document

###Naming Conventions
1. No abbreviations in variable, function, or directory names. (example: first_name instead of fir_na).
2. Variables start with nouns, functions/methods start with verbs.
3. Follow general Python naming conventions (ie snake_case for variables/module names, camelCase for classes, etc.)
4. A module should start with the layer it is in (ie data_customer or dal_customer).
   1. You may use an abbreviation of the layer in the module name.
      1. data access layer -> dal
      2. service layer -> serl
      3. API layer -> api

###Reporting and Fixing Bugs
1. Bugs should be reported via GitHub's Issues framework.
2. Title/comments should be formatted as follows
   1. Title: [Critical Level Name] - Module Name
   2. Comments: Error Message, Line Number, Initial Thoughts on 'Why'
   3. Assignees: Assign yourself, or reach out for help and assign others.
      1. Make sure other people know that they're being assigned to a bug.
3. Critical Level Definitions:
   1. Not Critical, more Quality of Life oriented
   2. Critical, but does not impede standard operating procedures
   3. Highly Critical, impedes standard operating procedures
4. Fix things from the highest critical level to the lowest critical level.
5. For this project, do not create sub-branches for bugfixing. However, branches must be bug free before they are
   merged into the main branch.
6. Once the bug is fixed, comment briefly how it was fixed, then click 'Close Issue with Comment' on the GitHub Issues page. 

###API Endpoints
1. Do not use abbreviations.
2. Do not use verbs in URIs (those will be in the header of the HTTP request).
3. General format is: <object>/<identifer>/etc (ie customer/5/account/7).
4. For cases not explicitly stated here, refer to RESTful conventions.

###Best Practices
1. Check the GitHub repository consistently.
2. Get some sleep and eat.
3. File structure should be as follows:
   1. Layer Directory (ie data_access_layer)
      1. all modules (ie dal_customer)
   There should be no directories within directories (except for custom_exceptions in utilities).
4. Communicate! :clap: