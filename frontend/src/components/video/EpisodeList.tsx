interface Episode {
  id: string
  title: string
  duration: string
}

interface EpisodeListProps {
  episodes: Episode[]
}

export default function EpisodeList({ episodes }: EpisodeListProps) {
  return (
    <div className="episode-list">
      <h3 className="text-xl font-bold mb-4">Episodes</h3>
      <ul className="space-y-2">
        {episodes.map((episode) => (
          <li key={episode.id} className="flex justify-between items-center p-2 bg-gray-100 rounded">
            <span>{episode.title}</span>
            <span className="text-sm text-gray-600">{episode.duration}</span>
          </li>
        ))}
      </ul>
    </div>
  )
}