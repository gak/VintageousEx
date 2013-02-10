import sublime
import sublime_plugin


class FooBarCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("HELLO WORLD FROM FOOBAR")
