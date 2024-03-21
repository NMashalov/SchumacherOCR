import nltk
import re

inline_reg = re.compile(r"\\\((.*?)(?<!\\)\\\)")
display_reg = re.compile(r"\\\[(.+?)(?<!\\)\\\]")


def compute_metrics(pred, gt, minlen=4):
    metrics = {}
    if len(pred) < minlen or len(gt) < minlen:
        return metrics
    metrics["edit_dist"] = nltk.edit_distance(pred, gt) / max(len(pred), len(gt))
    reference = gt.split()
    hypothesis = pred.split()
    metrics["bleu"] = nltk.translate.bleu([reference], hypothesis)
    try:
        metrics["meteor"] = nltk.translate.meteor([reference], hypothesis)
    except LookupError:
        metrics["meteor"] = np.nan
    reference = set(reference)
    hypothesis = set(hypothesis)
    metrics["precision"] = nltk.scores.precision(reference, hypothesis)
    metrics["recall"] = nltk.scores.recall(reference, hypothesis)
    metrics["f_measure"] = nltk.scores.f_measure(reference, hypothesis)
    return metrics