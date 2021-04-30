from . import utilities
import re


def get_filters():
    filters = {"test": TestsFilter(), "docs": DocumentationFilter(),
               "nonsource": NonSourceFilter()}
    return filters


class Filter():
    def __call__(self, path):
        pass


class TestsFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(tests?|spec)\b')

    def __call__(self, path):
        return not bool(self._regex.search(path))


class NonSourceFilter(Filter):
    def __init__(self):
        self._regex = self.create_regex()

    def __call__(self, path):
        return not bool(self._regex.search(path))

    def create_regex(self):
        nonsource_file_extensions = ["abnf", "apib", "asn", "asn1", "afm", "OutJob", "PcbDoc", "PrjPCB", "SchDoc", "apacheconf", "vhost", "asciidoc", "adoc", "asc", "avdl", "bib", "bibtex", "blade", "blade.php", "c-objdump", "cil", "dae", "cson", "css", "csv", "cabal", "soy", "conllu", "conll", "cppobjdump", "c++-objdump", "c++objdump", "cpp-objdump", "cxx-objdump", "creole", "cue", "d-objdump", "zone", "arpa", "darcspatch", "dpatch", "diff", "patch", "x", "ebnf", "ejs", "ect", "jst", "eml", "mbox", "sch", "brd", "eb", "epj", "edc", "flf", "for", "eam.fs", "ged", "gn", "gni", "gbr", "cmp", "gbl", "gbo", "gbp", "gbs", "gko", "gml", "gpb", "gpt", "gtl", "gto", "gtp", "gts", "ncl", "sol", "po", "pot", "gitconfig", "bdf", "gradle", "gml", "graphql", "gql", "graphqls", "dot", "gv", "cfg", "html", "htm", "html.hl", "inc", "xht", "xhtml", "ecr", "eex", "html.leex", "erb", "erb.deface", "rhtml", "phtml", "cshtml", "razor", "http", "hxml", "haml", "haml.deface", "handlebars", "hbs", "ini", "cfg", "dof", "lektorproject", "prefs", "pro", "properties", "irclog", "weechatlog", "gitignore", "json", "avsc", "geojson", "gltf", "har", "ice", "JSON-tmLanguage", "jsonl", "mcmeta", "tfstate", "tfstate.backup", "topojson", "webapp", "webmanifest", "yy", "yyp", "jsonc", "sublime-build", "sublime-commands", "sublime-completions", "sublime-keymap", "sublime-macro", "sublime-menu", "sublime-mousemap", "sublime-project", "sublime-settings", "sublime-theme", "sublime-workspace", "sublime_metrics", "sublime_session", "json5", "jsonld", "properties", "jinja", "j2", "jinja2", "ipynb", "kicad_pcb", "kicad_mod", "kicad_wks", "brd", "sch", "kit", "csl", "asy", "lark", "latte", "less", "ld", "lds", "x", "mod", "liquid", "mtml", "md", "markdown", "mdown", "mdwn", "mdx", "mkd", "mkdn", "mkdown", "ronn", "scd", "workbook", "marko", "mask", "dsp", "sln", "muse", "mustache", "neon", "nl", "nginx", "nginxconf", "vhost", "ninja", "njk", "objdump", "odin", "plist", "glyphs", "fea", "org", "pic", "chem", "pkl", "puml", "iuml", "plantuml", "pod", "pod", "pod6", "pcss", "postcss", "ps", "eps", "epsi", "pfa", "prisma", "pro", "proto", "asc", "pub", "jade", "pug", "pd", "pytb", "raml", "rdoc", "rmd",
                                     "spec", "rnh", "rno", "raw", "regexp", "regex", "rtf", "riot", "roff", "1", "1in", "1m", "1x", "2", "3", "3in", "3m", "3p", "3pm", "3qt", "3x", "4", "5", "6", "7", "8", "9", "l", "man", "mdoc", "me", "ms", "n", "nr", "rno", "tmac", "1", "1in", "1m", "1x", "2", "3", "3in", "3m", "3p", "3pm", "3qt", "3x", "4", "5", "6", "7", "8", "9", "man", "mdoc", "scss", "te", "sparql", "rq", "sql", "cql", "ddl", "inc", "mysql", "prc", "tab", "udf", "viw", "srt", "ston", "svg", "sass", "scaml", "slim", "sfd", "st", "styl", "srt", "sss", "svelte", "toml", "tsv", "tex", "aux", "bbx", "cbx", "cls", "dtx", "ins", "lbx", "ltx", "mkii", "mkiv", "mkvi", "sty", "toc", "tea", "texinfo", "texi", "txi", "txt", "fr", "nb", "ncl", "no", "textile", "ttl", "twig", "tl", "anim", "asset", "mask", "mat", "meta", "prefab", "unity", "txt", "snip", "snippet", "snippets", "vue", "mtl", "obj", "owl", "vtt", "mediawiki", "wiki", "wikitext", "reg", "toc", "xbm", "xpm", "pm", "xml", "adml", "admx", "ant", "axml", "builds", "ccproj", "ccxml", "clixml", "cproject", "cscfg", "csdef", "csl", "csproj", "ct", "depproj", "dita", "ditamap", "ditaval", "dll.config", "dotsettings", "filters", "fsproj", "fxml", "glade", "gml", "gmx", "grxml", "gst", "iml", "ivy", "jelly", "jsproj", "kml", "launch", "mdpolicy", "mjml", "mm", "mod", "mxml", "natvis", "ncl", "ndproj", "nproj", "nuspec", "odd", "osm", "pkgproj", "pluginspec", "proj", "props", "ps1xml", "psc1", "pt", "rdf", "res", "resx", "rs", "rss", "sch", "scxml", "sfproj", "shproj", "srdf", "storyboard", "sublime-snippet", "targets", "tml", "ts", "tsx", "ui", "urdf", "ux", "vbproj", "vcxproj", "vsixmanifest", "vssettings", "vstemplate", "vxml", "wixproj", "workflow", "wsdl", "wsf", "wxi", "wxl", "wxs", "x3d", "xacro", "xaml", "xib", "xlf", "xliff", "xmi", "xml.dist", "xmp", "xproj", "xsd", "xspec", "xul", "zcml", "plist", "stTheme", "tmCommand", "tmLanguage", "tmPreferences", "tmSnippet", "tmTheme", "xsp-config", "xsp.metadata", "yml", "mir", "reek", "rviz", "sublime-syntax", "syntax", "yaml", "yaml-tmlanguage", "yaml.sed", "yml.mysql", "yang", "yasnippet", "desktop", "desktop.in", "dircolors", "edn", "nanorc", "rst", "rest", "rest.txt", "rst.txt"]

        non_source_regex_segment = ''
        for extension in nonsource_file_extensions:
            non_source_regex_segment += (extension + '|')
        non_source_regex_segment = non_source_regex_segment[0:-1]
        # Expression looks for nonsource files in list and paths without extension
        return re.compile(r'^.*\.(" + non_source_regex_segment + ")|^[^\.]*$')


class DocumentationFilter(Filter):
    def __init__(self):
        self._regex = re.compile(r'\b(docs?)\b')

    def __call__(self, path):
        return not bool(self._regex.search(path))
