import customtkinter as ctk
from pages.widgets import SectionHeader, ACCENT


class GroupedPage(ctk.CTkFrame):
    """A top-level nav destination that hosts several related sub-pages,
    switchable via a segmented-button strip instead of being separate
    sidebar entries. Sub-pages are built lazily (only when this page is
    first shown) via factory functions, and reuse whatever page classes
    already exist (TweakCategoryPage, DebloatPage, etc.) completely unchanged.
    """

    def __init__(self, master, app, title, subtitle, sub_page_factories):
        """sub_page_factories: list of (label, factory) where factory(parent) -> CTkFrame page"""
        super().__init__(master, fg_color="transparent")
        self.app = app
        self.title_text = title
        self.subtitle_text = subtitle
        self.sub_page_factories = sub_page_factories
        self.order = [label for label, _ in sub_page_factories]
        self.sub_pages = {}
        self._built = False

    def on_show(self):
        if not self._built:
            self._build()
            self._built = True
        self._show_sub(self.segmented.get() or self.order[0])

    def _build(self):
        outer = ctk.CTkFrame(self, fg_color="transparent")
        outer.pack(fill="both", expand=True, padx=30, pady=24)

        SectionHeader(outer, self.title_text, self.subtitle_text).pack(
            anchor="w", fill="x", pady=(0, 16)
        )

        self.segmented = ctk.CTkSegmentedButton(
            outer, values=self.order, command=self._show_sub,
            selected_color=ACCENT, selected_hover_color=ACCENT,
            font=("Segoe UI", 13), height=36,
        )
        self.segmented.set(self.order[0])
        self.segmented.pack(anchor="w", pady=(0, 18))

        self.content_area = ctk.CTkFrame(outer, fg_color="transparent")
        self.content_area.pack(fill="both", expand=True)
        self.content_area.grid_columnconfigure(0, weight=1)
        self.content_area.grid_rowconfigure(0, weight=1)

        for label, factory in self.sub_page_factories:
            page = factory(self.content_area)
            page.grid(row=0, column=0, sticky="nsew")
            self.sub_pages[label] = page

    def _show_sub(self, label):
        self.segmented.set(label)
        page = self.sub_pages[label]
        page.tkraise()
        if hasattr(page, "on_show"):
            page.on_show()
