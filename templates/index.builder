xml.instruct!
xml.feed "xmlns" => "http://www.w3.org/2005/Atom" do
  xml.title 'Fooberry.com' #@config[:title]
  xml.id "http://fooberry.com" 
  xml.updated articles.last[:date].iso8601 unless articles.empty?
  xml.author { xml.name @config[:author] }

  articles.reverse[0...10].each do |article|
    xml.entry do
      xml.title article.title
      xml.link "rel" => "alternate", "href" => "http://fooberry.com" +  article.path
      xml.id "http://fooberry.com" +  article.path
      xml.published article[:date].iso8601
      xml.updated article[:date].iso8601
      xml.author { xml.name @config[:author] }
      xml.summary article.summary, "type" => "html"
      xml.content article.body, "type" => "html"
    end
  end
end

