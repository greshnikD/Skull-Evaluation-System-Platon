package ru.gmed.cms.db.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.hibernate.annotations.Generated;
import org.hibernate.annotations.GenerationTime;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.data.annotation.CreatedDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;
import javax.persistence.Version;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Entity
@NoArgsConstructor
@Builder
@Getter
@Setter
public class Research {
    @Id
    @Column(name = "id", nullable = false)
    @Generated(GenerationTime.ALWAYS)
    private UUID id;

    @OneToMany(mappedBy = "id", fetch = FetchType.LAZY)
    private List<ResearchFile> researchFileList = new ArrayList<>();
    @OneToOne(fetch = FetchType.LAZY)
    private Patient patient;
    @OneToOne(fetch = FetchType.LAZY)
    private Doctor doctor;

    @CreatedDate
    private LocalDateTime createDate;
    @UpdateTimestamp
    private LocalDateTime updateDate;
    @Version
    private Integer version;
    private LocalDateTime deleteDate;
    private boolean deleted;
}
