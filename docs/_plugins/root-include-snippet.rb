class RootIncludeSnippet < Liquid::Tag
  def initialize(_tag_name, markup, _parse_context)
    super
    @markup = markup.strip
  end

  def render(context)
    expanded_path = Liquid::Template.parse(@markup).render(context)
    root_path = File.expand_path(context.registers[:site].config['source'])
    final_path = File.join(root_path, expanded_path)
    file_read_opts = context.registers[:site].file_read_opts

    read_lines_from_file(final_path, file_read_opts)
  end

  def read_lines_from_file(file_path, file_read_opts)
    lines = []
    in_section = false

    File.foreach(file_path, **file_read_opts) do |line|
      # print(file_path)
      if line.include?('# given')
        in_section = true
      elsif line.include?('# then')
        break
      end
      # line.sub!(/^\t{2}/, "")
      line.sub!(/^ {8}/, "")
      lines << line if in_section
    end
    # print(lines)
    # lines << '# then'
    lines.pop
    lines
  end
end

Liquid::Template.register_tag('root_include_snippet', RootIncludeSnippet)