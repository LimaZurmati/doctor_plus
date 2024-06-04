## Manual Testing

*For any Fails, there is a more detailed description below the table*

ADMIN
| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Blog Post | Post successfully created and displayed home | Pass |
| Edit Blog Post | Post content and category updated successfully | Pass |
| Delete Blog Post | Post deleted successfully | Pass |
| Add about information | added successfully | Pass |
| Delete User Comments | Comment deleted successfully | Pass |
| Approve comments | Approved successfully | Pass |


(*) - While testing the ability to edit posts (Limited to Admin only), I had a problem when editing the title and slug of the post. This was due to the URL not being able to find the original slug of the post (because it had been changed during the edit) to route it after the editing was complete. At this stage, I felt the easiest fix was to remove the ability to edit the post title and slug in the browser, but this functionality is still available via the django admin panel.

## User

| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Account | Created successfully | Pass |
| Login | Login Successful | Pass |
| Logout | Logout Successful | Pass |
| Read Full doctor Post | PostDetail page loaded successfully | Pass |
| Add Comment under post details | Comment Added Successfully | Pass |
| Delete Comment | Comment Deleted | Pass |
| Update Comment | Comment Updated | Pass |
| Create User Account to leave comment| commented successfully | Pass |