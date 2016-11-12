from i3pystatus import get_module, Status

status = Status()

# Note that the 'self' parameter is required and gives access to all
# variables of the module.
@get_module
def change_text(self):
    self.output["full_text"] = "Clicked"

status.register("text",
    text = "Initial text",
    on_leftclick = [change_text],
    # or
    on_rightclick = change_text,
    )

status.run()