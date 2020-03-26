from revscoring.dependencies import solve

from revscoring.datasources import revision_oriented as ro
from ..diff import operations_context


A = """I am some interesting text. I mostly represent a
paragraph. There's something that is going to change right about here. But then
the paragraph picks up again and there's some more stuff to think about.  Isn't
that interesting? I think it's interesting. Here's a citation for why it is
interesting: <ref name="me"> M. E., I think this is all quite interesting.
Journal of Self Reference. 42:1.</ref>""".replace("\n", " ")

B = """I am some interesting text. I mostly represent a
paragraph. There's something that is going to change right about there. But
then the paragraph picks up again and there's some more stuff to think about.
Isn't that interesting? I think it's interesting. Here's a citation for why it
is interesting: <ref name="me"> M. E., I think this is all quite interesting.
Journal of Self Reference. 42:1.</ref>""".replace("\n", " ")


def test_operations_context():
    cache = {
        ro.revision.text: A,
        ro.revision.parent.text: B
    }

    contexts = solve(operations_context, cache=cache)

    assert not contexts[0]
    assert len(contexts[1]), 93
    assert "there" in contexts[1]
    assert len(contexts[2]), 93
    assert "here" in contexts[2]
    assert not contexts[3]


'''
def test_added_segments_context():
    cache = {
        revision.text: A,
        parent_revision.text: B
    }

    eq_(
        solve(added_segments_context, cache=cache),
        ["I am some interesting text. I mostly represent a paragraph. " +
         "There's something that is going to change right about here. But " +
         "then the paragraph picks up again and there's some more stuff to " +
         "think about. Isn't that interesting? I think it'"]
    )

def test_removed_segments_context():
    cache = {
        revision.text: A,
        parent_revision.text: B
    }

    eq_(
        solve(removed_segments_context, cache=cache),
        ["I am some interesting text. I mostly represent a paragraph. " +
         "There's something that is going to change right about there. But " +
         "then the paragraph picks up again and there's some more stuff to " +
         "think about. Isn't that interesting? I think it'"]
    )
'''
test_operations_context()
