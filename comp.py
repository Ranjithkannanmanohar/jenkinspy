import difflib
import time

with open('devices.txt') as routers:
    for IP in routers:
        lines = routers.readlines()

def compare():
    show_pre = "Show_pre"
    show_post = "Show_post"
    show_pre_lines = open("./" +IP + "_pre.txt").readlines()
    time.sleep(0.5)
    show_post_lines = open("./" +IP + "_post.txt").readlines()
    time.sleep( 0.5 )
    difference = difflib.HtmlDiff(wrapcolumn=80).make_file(show_pre_lines, show_post_lines,show_pre,show_post)
    difference_report = open("./show_comparison.xml", "w+")
    difference_report.write(difference)
    difference_report.close()
    time.sleep(0.5)

compare()

print("Task Completed.")
